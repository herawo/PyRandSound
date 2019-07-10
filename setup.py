import setuptools
from PyRandSound import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

CLASSIFIERS = [
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name="pypeertube",
    version=__version__,
    author="Webu",
    author_email="clemalex20@gmail.com",
    description="PyRandSound; python library to generate random sound effects",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/herawo/PyRandSound",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=[
        'pygame==1.9.6',
    ],
    zip_safe=False,
)
