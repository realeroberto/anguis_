# anguis

[![PyPI](https://img.shields.io/pypi/v/anguis.svg)](https://pypi.org/project/anguis/)

*Latet anguis in herba* (Virgil, *Eclogues*, 3, 93)

**anguis** is a distributed assert system over etcd.


## Installation

From source:

        $ python setup.py install

From PyPI:

        $ pip3 install anguis


## Example of usage

```
from anguis import anguisEtcd

cache = anguisEtcd.AnguisEtcd()

cache.set('foo', 'bar')
print(cache.get('foo'))
# bar

cache.erase('foo')
print(cache.get('foo'))
# None
```
