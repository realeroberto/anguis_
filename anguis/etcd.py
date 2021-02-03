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

import etcd3
from anguis.base import AnguisBase

class AnguisEtcd(AnguisBase):

    def __init__(self, host='localhost', port=2379):
        self.etcd = etcd3.client(host, port)
        super(AnguisEtcd, self).__init__()

    def __del__(self):
        super(AnguisEtcd, self).__del__()
        self.etcd.close()

    def __getitem__(self, key):
        return self.etcd.get(key)[0]

    def __setitem__(self, key, value):
        return self.etcd.put(key, value)

    def __delitem__(self, key):
        return self.etcd.delete(key)

    def __iter__(self):
        return iter([m.key for (_, m) in self.etcd.get_all()])

    def __len__(self):
        return sum(1 for _ in self.etcd.get_all())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
