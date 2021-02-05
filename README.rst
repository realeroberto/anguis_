======
anguis
======

.. image:: https://img.shields.io/pypi/v/anguis.svg
        :target: https://pypi.python.org/pypi/anguis

.. image:: https://img.shields.io/travis/reale/anguis.svg
        :target: https://travis-ci.com/reale/anguis

.. image:: https://readthedocs.org/projects/anguis/badge/?version=latest
        :target: https://anguis.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/reale/anguis/shield.svg
     :target: https://pyup.io/repos/github/reale/anguis/
     :alt: Updates

*Latet anguis in herba* (Virgil, *Eclogues*, 3, 93)

**anguis** is a generic key-store library in Python.

Currently, the following backends are supported:

-  filesystem
-  Etcd
-  Git
-  Redis
-  memcached
-  SFTP
-  Sqlite
-  Google Drive

Rationale
---------

TODO

Installation
------------

From source:

::

    $ python setup.py install

From PyPI:

::

    $ pip3 install anguis

Example of usage
----------------

::

    from anguis.fs import AnguisFS

    cache = AnguisFS()

    cache['foo'] = 'bar'
    print(cache['foo'])
    # bar

    del(cache['foo'])
    print(cache['foo'])
    # None
