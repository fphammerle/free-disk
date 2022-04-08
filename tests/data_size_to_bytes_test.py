import pytest

import free_disk

# pylint: disable=protected-access; tests


@pytest.mark.parametrize(
    ("data_size_with_unit", "expected_bytes"),
    [
        ("123", 123),
        ("123B", 123),
        ("123.0B", 123),
        ("1kB", 1000),
        ("2kB", 2000),
        ("2.5kB", 2500),
        ("2KB", 2000),
        ("8MB", 8 * (10**6)),
        ("8.5MB", 8.5 * (10**6)),
        ("32GB", 32 * (10**9)),
        ("9TB", 9 * (10**12)),
        ("3KiB", 3 * (1024**1)),
        ("40MiB", 40 * (1024**2)),
        ("512GiB", 512 * (1024**3)),
        ("7TiB", 7 * (1024**4)),
        ("123 B", 123),
        ("123\tB", 123),
        ("123.0  B", 123),
        ("1  kB", 1000),
        ("1  MiB", 1024**2),
    ],
)
def test__data_size_to_bytes(data_size_with_unit: str, expected_bytes: int) -> None:
    assert expected_bytes == free_disk._data_size_to_bytes(data_size_with_unit)


@pytest.mark.parametrize("data_size_with_unit", ["abcdef", "123G"])
def test__data_size_to_bytes_fail(data_size_with_unit: str) -> None:
    with pytest.raises(ValueError):
        free_disk._data_size_to_bytes(data_size_with_unit)
