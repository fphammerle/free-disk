import subprocess


def test_entrypoint():
    assert subprocess.run(
        ["free-disk", "--help"], stdout=subprocess.PIPE, check=True
    ).stdout.startswith(b"usage: ")
