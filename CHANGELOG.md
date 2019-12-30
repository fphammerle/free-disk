# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2019-12-30
### Added
- package: use readme as long description

### Fixed
- added missing timezone identifier to log message
- removed module import from `setup.py`

## [0.2.0] - 2019-04-27
### Added
- `--free-bytes` now supports human-readable formats like '2TB' or '2GiB'

### Fixed
- fix: ModuleNotFoundError after installation

## [0.1.0] - 2019-04-27
`free-disk --debug --free-bytes 1234 /dir/to/cleanup`

[Unreleased]: https://github.com/fphammerle/free-disk/compare/0.2.1...HEAD
[0.2.1]: https://github.com/fphammerle/free-disk/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/fphammerle/free-disk/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/fphammerle/free-disk/tree/0.1.0
