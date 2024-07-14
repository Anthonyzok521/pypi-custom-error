'''Setup'''
from setuptools import setup, find_packages

with open('./README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='custom_error',
    version='1.0.0',
    description='Create your custom errors and I have control of them with Custom Error',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Anthony Carrillo',
    author_email='anthonyzok521@gmail.com',
    url='https://github.com/Anthonyzok521/pypi-custom-error',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"", "src"},
    packages=find_packages(where="src")
)
