#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


setup(
    name='elophant',
    version='0.0.3',
    description='API Wrapper for Elophant(.com)',
    long_description=open('README.rst').read(),
    author='Bryan Veloso',
    author_email='bryan@revyver.com',
    url='https://github.com/bryanveloso/elophant.py',
    py_modules=['elophant'],
    install_requires=['requests'],
    license='MIT',
)
