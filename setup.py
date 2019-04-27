import setuptools

setuptools.setup(
    name='free-disk',
    use_scm_version=True,
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
        # TODO add classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
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
    ],
)
