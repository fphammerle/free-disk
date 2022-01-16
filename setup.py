import pathlib

import setuptools

setuptools.setup(
    name="free-disk",
    use_scm_version=True,
    description="delete file with oldest modification date"
    " until a minimum of --free-bytes are available on disk",
    # Path.read_text() new in python v3.5
    long_description=pathlib.Path(__file__).parent.joinpath("README.md").read_text(),
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
        # .github/workflows/python.yml
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "free-disk = free_disk:_main",
        ],
    },
    # >=3.5 pathlib.Path.read_text()
    # >=3.6 f-strings
    # <3.7 untested
    python_requires=">=3.7",
    install_requires=[],
    setup_requires=["setuptools_scm"],
    tests_require=["pytest"],
)
