#!/usr/bin/env python3

from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='brainfoose',
    version='2.0.1',
    description='A brainfuck REPL.',
    long_description=long_description,
    url='https://github.com/awesmubarak/brainfoose',
    author='Awes Mubarak',
    author_email='awes.mubarak@awesmubarak.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    keywords='brainfuck esoteric programming language repl',
    packages=['brainfoose'],
    entry_points={
        "console_scripts": [
            "brainfoose=brainfoose:main"
        ],
    },
    install_requires=['docopt', 'termcolor']
)
