import pathlib

import setuptools


def _read_text(path: pathlib.Path) -> str:
    with path.open("r") as file:
        return file.read()


setuptools.setup(
    name="free-disk",
    use_scm_version=True,
    description="delete file with oldest modification date"
    " until a minimum of --free-bytes are available on disk",
    # Path.read_text() new in python v3.5
    long_description=_read_text(pathlib.Path(__file__).parent.joinpath("README.md")),
    long_description_content_type="text/markdown",
    author="Fabian Peter Hammerle",
    author_email="fabian@hammerle.me",
    url="https://github.com/fphammerle/free-disk",
    license="MIT",
    keywords=[
        "disk",
        "files",
        "cleanup",
        "free",
        "delete",
        "old",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "free-disk = free_disk:main",
        ],
    },
    install_requires=[],
    # workaround pipenv ignoring setuptools-scm's python version requirement
    # https://github.com/pypa/setuptools_scm/blob/v6.0.0/setup.cfg#L31
    # https://github.com/pypa/setuptools_scm/commit/a16bae72c89c8ebebdb66d91f22bc2673b919070#diff-cfca63f0fb5632710d835abfc6665a033235fd9f92a81d25cb6fad0873ffe2b6R42
    # https://travis-ci.org/github/fphammerle/free-disk/jobs/766438074#L237
    setup_requires=["setuptools_scm<6"],
    tests_require=["pytest"],
)
