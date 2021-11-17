from setuptools import setup, find_packages

setup(
    name='DataImportTool',
    version='0.0.1',
    packages=find_packages(include=['dit','dit.core']),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'dit = dit.main:main',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
