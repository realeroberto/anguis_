#!/usr/bin/env python

# anguis - A generic key-store library

# The MIT License (MIT)
# 
# Copyright (c) 2018-21 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from unittest import TestCase

from anguis.fs import *
from anguis.etcd import *
from anguis.git_ import *
from anguis.gdrive import *
from anguis.redis_ import *
from anguis.sftp import *
from anguis.sqlite import *

class Test(TestCase):
    def testFS(self):
        cache = AnguisFS(autoDestroy=True)

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testEtcd(self):
        cache = AnguisEtcd()

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testGit(self):
        cache = AnguisGit(dir='/tmp/git')

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testGdrive(self):
        cache = AnguisGdrive()

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testMemcached(self):
        cache = AnguisMemcached()

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testRedis(self):
        cache = AnguisRedis()

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testSFTP(self):
        hostname = os.environ['SFTP_HOSTNAME']
        username = os.environ['SFTP_USERNAME']
        password = os.environ['SFTP_PASSWORD']
        dir = os.environ['SFTP_DIR']

        cache = AnguisSFTP(hostname, username, password, dir)

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')

    def testSqlite(self):
        cache = AnguisSqlite()

        cache['foo'] = 'bar'
        self.assertTrue(cache['foo'] == 'bar')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
