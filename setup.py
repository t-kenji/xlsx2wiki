#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from xlsx2wiki.version import __version__ as VERSION

setup(
    name = 'xlsx2wiki',
    version = VERSION,
    description = 'xlsx file contents transform to Trac wiki table',
    author = 't-kenji',
    author_email = 'protect.2501@gmail.com',
    license = 'BSD',
    url = 'https://github.com/t-kenji/xlsx2wiki',

    packages = find_packages(exclude=['*.tests', 'tests.*', '*.tests.*']),
    package_data = {
        'xlsx2wiki': [
            'templates/*.jinja',
        ],
    },

    install_requires = [
        'openpyxl',
        'jinja2',
    ],

    entry_points = {
        'console_scripts': {
            'xlsx2wiki = xlsx2wiki.console:run',
        },
    }
)
