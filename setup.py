from setuptools import setup, find_packages

setup(
    name='DataImportTool',
    version='0.0.2',
    packages=find_packages(include=['src']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dit = src.main:main',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
