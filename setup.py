#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

package_name = "SecutiryGenPuzzle"
# consider the path of `setup.py` as root directory:
PROJECTROOT = os.path.dirname(sys.argv[0]) or "."


with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
