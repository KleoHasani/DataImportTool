from setuptools import setup, find_packages

setup(
    name='DataImportTool',
    version='0.0.3',
    packages=find_packages(include=['dit']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
