# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='advent_of_code',
    version='0.1.0',
    description='Advent of Code Puzzle Solver',
    long_description=readme,
    author='Sven Meisel',
    author_email='vip3out@pm.me',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)