# free-disk

[![Build Status](https://travis-ci.org/fphammerle/free-disk.svg?branch=master)](https://travis-ci.org/fphammerle/free-disk)

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
