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
    keywords=["disk", "files", "cleanup", "free", "delete", "old",],
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
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["free-disk = free_disk:main",],},
    install_requires=[],
    setup_requires=["setuptools_scm",],
    tests_require=["pylint>=2.3.0", "pytest",],
)
