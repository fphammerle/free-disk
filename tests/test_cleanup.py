import collections
import logging
import pathlib
import unittest.mock

import _pytest.logging
import free_disk

# pylint: disable=protected-access

_DiskUsage = collections.namedtuple("_DiskUsage", ("free",))


def _folder_size_bytes(path: pathlib.Path) -> int:
    return sum(p.stat().st_size for p in path.rglob("*"))


def test__main_remove_some(
    caplog: _pytest.logging.LogCaptureFixture, tmp_path: pathlib.Path
) -> None:
    tmp_path.joinpath("a").write_bytes(b"a" * 4)
    tmp_path.joinpath("b").write_bytes(b"b" * 3)
    tmp_path.joinpath("c").write_bytes(b"c" * 5)
    tmp_path.joinpath("d").write_bytes(b"d" * 2)
    tmp_path.joinpath("e").write_bytes(b"d" * 7)
    with unittest.mock.patch(
        "shutil.disk_usage",
        lambda p: _DiskUsage(free=42 - _folder_size_bytes(tmp_path)),
    ), unittest.mock.patch(
        "sys.argv", ["", "--free-bytes", "30B", str(tmp_path)]
    ), caplog.at_level(
        logging.DEBUG
    ):
        free_disk._main()
    assert {p.name for p in tmp_path.rglob("*")} == {"e", "d"}
    assert caplog.record_tuples[:-1] == [
        ("root", logging.DEBUG, m)
        for m in [
            "Required free bytes: 30",
            "_DiskUsage(free=21)",
            f"Removed file {tmp_path.joinpath('a')}",
            f"Removed file {tmp_path.joinpath('b')}",
            f"Removed file {tmp_path.joinpath('c')}",
        ]
    ]
    assert caplog.records[-1].levelno == logging.INFO
    assert caplog.records[-1].message.startswith(
        "Removed 3 file(s) with modification date <= 20"
    )


def test__main_sufficient_space(
    caplog: _pytest.logging.LogCaptureFixture, tmp_path: pathlib.Path
) -> None:
    tmp_path.joinpath("a").write_bytes(b"a" * 4)
    tmp_path.joinpath("b").write_bytes(b"b" * 3)
    tmp_path.joinpath("c").write_bytes(b"c" * 5)
    with unittest.mock.patch(
        "shutil.disk_usage",
        lambda p: _DiskUsage(free=42 - _folder_size_bytes(tmp_path)),
    ), unittest.mock.patch(
        "sys.argv", ["", "--free-bytes", "30B", str(tmp_path)]
    ), caplog.at_level(
        logging.DEBUG
    ):
        free_disk._main()
    assert {p.name for p in tmp_path.rglob("*")} == {"a", "b", "c"}
    assert caplog.record_tuples == [
        ("root", logging.DEBUG, "Required free bytes: 30"),
        ("root", logging.DEBUG, "_DiskUsage(free=30)"),
        ("root", logging.DEBUG, "Requirement already fulfilled"),
    ]


def test__main_no_files(
    caplog: _pytest.logging.LogCaptureFixture, tmp_path: pathlib.Path
) -> None:
    with unittest.mock.patch(
        "shutil.disk_usage", return_value=_DiskUsage(free=21)
    ), unittest.mock.patch(
        "sys.argv", ["", "--free-bytes", "30B", str(tmp_path)]
    ), caplog.at_level(
        logging.DEBUG
    ):
        free_disk._main()
    assert caplog.record_tuples == [
        ("root", logging.DEBUG, "Required free bytes: 30"),
        ("root", logging.DEBUG, "_DiskUsage(free=21)"),
        ("root", logging.WARNING, "No files to remove"),
    ]