from setuptools import setup, find_packages

setup(
    name='DataImportTool',
    version='0.0.3',
    packages=find_packages(include=['src']),
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'dit = src.main:cli',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
