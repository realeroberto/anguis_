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
import random
import string
import stat
import paramiko
from anguis.base import AnguisBase

class AnguisSFTP(AnguisBase):

    def _key_to_path(self, key):
        return os.path.join(self.dir, key)

    def _string_generator(self, size=20,
            chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def _isdir(self, path):
        mode = self.sftp.stat(path).st_mode
        return S_ISDIR(mode)

    def _rmtree(self, base):
        # XXX sometimes listdir() hangs
        for entry in self.sftp.listdir(base):
            path = os.path.join(base, entry)
            if self._isdir(path):
                self._rmtree(path)
            else:
                self.sftp.remove(path)
        self.sftp.rmdir(base)

    def __init__(self, hostname, username, password,
            dir=None, autoAddPolicy=True, autoDestroy=False):
        self.autoDestroy = autoDestroy
        # open ssh connection
        self.ssh = paramiko.SSHClient()
        if autoAddPolicy:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=hostname,username=username,password=password)
        self.sftp = self.ssh.open_sftp()
        # set remote directory
        if not dir:
            dir = self._string_generator()
            self.sftp.mkdir(dir)
        self.dir = dir
        # call parent constructor
        super(AnguisSFTP, self).__init__()

    def __del__(self):
        super(AnguisSFTP, self).__del__()
        if self.autoDestroy:
            self._rmtree(self.dir)
        if self.ssh:
            self.ssh.close()

    def __getitem__(self, key):
        try:
            with self.sftp.open(self._key_to_path(key), "r") as h:
                return h.readline()
        except: # TODO: test for errors
            return None
        return self.r.get(key)

    def __setitem__(self, key, value):
        with self.sftp.open(self._key_to_path(key), "w") as h:
            return h.write("%s" % value)

    def __delitem__(self, key):
        return self.sftp.remove(self._key_to_path(key))

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
