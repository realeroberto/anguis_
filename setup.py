from setuptools import setup

setup(
    name = 'anguis',
    version = '0.1',
    description = 'A generic key-store library',
    packages = [ 'anguis' ],
    author = 'Roberto Reale',
    author_email = 'rober.reale@gmail.com',
    url = 'https://github.com/robertoreale/anguis',
    keywords = [ 'cache', 'key-value store' ],
    install_requires = [ 'gitpython', 'paramiko', 'redis' ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
