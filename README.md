# anguis

[![PyPI](https://img.shields.io/pypi/v/anguis.svg)](https://pypi.python.org/pypi/anguis)

*Latet anguis in herba* (Virgil, *Eclogues*, 3, 93)

**anguis** is a generic key-store library in Python.

Currently, the following backends are supported:

* filesystem
* SFTP
* Git
* Redis


## Installation

From source:

        $ python setup.py install

From PyPI:

        $ pip3 install anguis


## Example of usage

```
from anguis import anguisFS

cache = anguisFS.AnguisFS()

cache.set('foo', 'bar')
print(cache.get('foo'))
# bar

cache.erase('foo')
print(cache.get('foo'))
# None
```
