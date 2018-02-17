# anguis

[![PyPI](https://img.shields.io/pypi/v/anguis.svg)](https://pypi.python.org/pypi/anguis)

*Latet anguis in herba* (Virgil, *Eclogues*, 3, 93)

**anguis** is a generic key-store library in Python.

## Usage

### File-system based cache

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

### SFTP based cache

```
from anguis import anguisSFTP

cache = anguisSFTP.AnguisSFTP('localhost', 'username', 'password')

cache.set('foo', 'bar')
print(cache.get('foo'))
# bar

cache.erase('foo')
print(cache.get('foo'))
# None
```

### Redis based cache

```
from anguis import anguisRedis

cache = anguisRedis.AnguisRedis()

cache.set('foo', 'bar')
print(cache.get('foo'))
# b'bar'

cache.erase('foo')
print(cache.get('foo'))
# None
```
