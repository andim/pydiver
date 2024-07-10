[![License](https://img.shields.io/pypi/l/python-diver.svg)](https://github.com/andim/pydiver/blob/main/LICENSE)
[![Latest release](https://img.shields.io/pypi/v/python-diver.svg)](https://pypi.python.org/pypi/python-diver)
[![Build Status](https://app.travis-ci.com/andim/pydiver.svg?branch=main)](https://app.travis-ci.com/andim/pydiver)
[![Documentation Status](https://readthedocs.org/projects/pydiver/badge/?version=latest)](https://pydiver.readthedocs.io/en/latest/?badge=latest)

# PyDiver: Ecological diversity analysis in python

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

## Citing PyDiver

If this software is useful to you please cite the following article, which derives and benchmarks the unbiased variance estimator:

Tiffeau-Mayer, A., 2024. Unbiased estimation of sampling variance for Simpson's diversity index. Physical Review E, 109(6), p.064411, [doi:PhysRevE.109.064411](https://doi.org/10.1103/PhysRevE.109.064411)
