#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='swim',
    version='0.1.0',
    description='swim',
    url='https://github.com/kylef/swim',
    packages=find_packages(),
    package_data={
    },
    entry_points={
        'console_scripts': [
            'swim = swim:cli',
        ]
    },
    install_requires=[
        'click',
    ],
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    license='BSD',
    classifiers=(
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'License :: OSI Approved :: BSD License',
    )
)

