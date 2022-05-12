# free-disk 💾

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI Pipeline Status](https://github.com/fphammerle/free-disk/workflows/tests/badge.svg)](https://github.com/fphammerle/free-disk/actions)
[![Last Release](https://img.shields.io/pypi/v/free-disk.svg)](https://pypi.org/project/free-disk/#history)
[![Python Version](https://img.shields.io/pypi/pyversions/free-disk.svg)](https://pypi.org/project/free-disk/)

Delete file with the oldest modification date
until a minimum of `--free-bytes` are available on the respective disk.

## Install

```sh
pip3 install --user --upgrade free-disk
```

## Usage

```sh
free-disk --help
free-disk --free-bytes 1GiB /dir/to/cleanup
free-disk --free-bytes 1GiB --delete-path-regex '\.mp4$' /dir/to/cleanup
free-disk --debug --free-bytes 2GB /dir/to/cleanup
```

## Tests

```sh
pip3 install --user pipenv
git clone https://github.com/fphammerle/free-disk.git
cd freesurfer-volume-reader
pipenv run pylint free_disk
pipenv run pytest
```
