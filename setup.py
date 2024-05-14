from setuptools import find_packages, setup

setup(
    name="autodir",
    packages=find_packages(include=['autodir']),
    version="1.1.0",
    description="Automatically switch directories, simply.",
    author="HyperSource",
    install_requires=['pathlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pathlib'],
    test_suite='tests',   
)