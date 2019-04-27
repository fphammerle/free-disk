import setuptools

import free_disk

setuptools.setup(
    name='free-disk',
    use_scm_version=True,
    description=free_disk.__doc__,
    author='Fabian Peter Hammerle',
    author_email='fabian@hammerle.me',
    url='https://github.com/fphammerle/free-disk',
    license='MIT',
    keywords=[
        'disk',
        'files',
        'cleanup',
        'free',
        'delete',
        'old',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'free-disk = free_disk:main',
        ],
    },
    install_requires=[],
    setup_requires=[
        'setuptools_scm',
    ],
    tests_require=[
        'pylint>=2.3.0',
        'pytest',
    ],
)
