#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='xdotool',
    version='0.0.1',
    description='',
    author='Ilya Chistyakov',
    author_email='ilchistyakov@gmail.com',
    packages=find_packages(exclude=('example',)),
)
