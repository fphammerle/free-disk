import subprocess


def test_entrypoint() -> None:
    assert subprocess.run(
        ["free-disk", "--help"], stdout=subprocess.PIPE, check=True
    ).stdout.startswith(b"usage: ")
