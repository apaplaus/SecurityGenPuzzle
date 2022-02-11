#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    name="SecurityGenPuzzle",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
