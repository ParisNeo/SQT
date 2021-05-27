from pathlib import Path
from typing import Union

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="sqtui",
    version="0.0.2",
    author="Saifeddine ALOUI",
    author_email="aloui.saifeddine@gmail.com",
    description="Safe QT, a QT wrapper for automatic selection of python QT libs (PyQt, PySide)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ParisNeo/SQTUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
