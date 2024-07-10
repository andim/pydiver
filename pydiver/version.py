from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 1
_version_minor = 0
_version_micro = ''  # use '' for first of series, number for 1 and above
#_version_extra = 'dev'
_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 3",              
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "Pydiver: ecological diversity analysis in Python" 
# Long description will go up on the pypi page
long_description = """
# PyDiver: ecological diversity analysis in Python

PyDiver is a lightweight software package for calculating Simpson diversity with error bars.

It provides a reference implementation of the unbiased variance estimates proposed in [Tiffeau-Mayer 2024](https://doi.org/10.1103/PhysRevE.109.064411).

## Installation

The quickest way to install Pyrepseq is via pip:

`pip install python-diver`

Note that this package is called python-diver on PyPI.

## Documentation and examples

You can find API documentation on [readthedocs](https://pydiver.readthedocs.io/en/latest/?badge=latest).
You can also create a local copy of the API documentation by running:

```bash
make html
```

in the docs folder.

You can find usage examples by looking at the code in the [pub_simpsonvar](https://github.com/andim/pydiver/tree/main/pub_simpsonvar) directory.
"""

NAME = "python-diver"
MAINTAINER = "Andreas Tiffeau-Mayer"
MAINTAINER_EMAIL = "andimscience@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://pydiver.readthedocs.io/"
DOWNLOAD_URL = "http://github.com/andim/pydiver"
LICENSE = "MIT"
AUTHOR = "Andreas Tiffeau-Mayer"
AUTHOR_EMAIL = "andimscience@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGES = ['pydiver']
REQUIRES = ["numpy"]
