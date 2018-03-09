# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from setuptools import setup, find_packages


setup(
    name='pootle_index',
    version='0.0.1',
    description='Pootle haystack search integration',
    long_description="Integration between Pootle and haystack backends",
    url='https://github.com/translate/pootle_index',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL3',
        'Programming Language :: Python :: 2.7'],
    keywords='pootle index search elasticsearch haystack',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['django-haystack==2.8.0', 'pootle'])
