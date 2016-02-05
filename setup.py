#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
from setuptools.command.develop import develop
import sys

packages = find_packages()
version_str = '5.5.0'

if sys.version_info.major < 3:
    langcodes_req = 'langcodes-py2 == 1.1.2'
else:
    langcodes_req = 'langcodes == 1.1.2'


setup(
    name = 'ConceptNet',
    version = version_str,
    description = 'A semantic network of general knowledge',
    author = "Rob Speer",
    author_email = 'conceptnet@media.mit.edu',
    packages=packages,
    include_package_data=True,
    exclude_package_data={'conceptnet5': ['support_data/testdata']},
    install_requires=[
        'xmltodict', 'click', 'pyyaml', 'requests', 'limits',
        'flask', 'flask-cors', 'flask-limiter', 'grako > 3', 'ftfy',
        'msgpack-python', langcodes_req
    ],
    # assoc-space >= 1.0b1 is required for using assoc-space features, but it's
    # not required for all of ConceptNet
    license = 'Apache License 2.0',
    entry_points = {
        'console_scripts': [
            'cn5-vectors = conceptnet5.vectors.cli:cli',
            'cn5-build-table = conceptnet5.hashtable.cli:run_build',
        ]
    }
)
