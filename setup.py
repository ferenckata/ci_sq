from setuptools import setup, find_packages


requirements = ['biopython']

setup(
    install_requires=requirements,
    name="cisq",
    version="0.0.1",
    packages=find_packages()
)
