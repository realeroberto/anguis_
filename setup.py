#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        'gitpython',
        'paramiko',
        'etcd3',
        'redis',
        'sqlitedict',
        'pymemcache',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
        ]

setup_requirements = [ ]

test_requirements = [ 'nose' ]

setup(
    author="Roberto Reale",
    author_email='roberto@reale.me',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A generic key-store library.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords = [ 'anguis', 'cache', 'key-value store' ],
    name='anguis',
    packages=find_packages(include=['anguis', 'anguis.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/reale/anguis',
    version='0.3.5',
    zip_safe=False,
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
