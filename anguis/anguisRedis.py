#!/usr/bin/env python

# anguis - A generic key-store library

# The MIT License (MIT)
# 
# Copyright (c) 2018 Roberto Reale
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

from redis.client import Redis
from anguis import anguisBase

class AnguisRedis(anguisBase.AnguisBase):

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        return self.r.set(key, value)

    def erase(self, key):
        return self.r.delete(key)

    def exists(self, key):
        return (self.r.exists(key) > 1)

    def keys(self):
        return self.r.keys()

    def randomkey(self):
        return self.r.randomkey()

    def rename(self, key, newkey):
        return self.r.rename(key, newkey)

    def touch(self, key):
        return self.r.touch(key)

    def __init__(self, host='localhost', port=6379, db=0):
        self.r = Redis(host, port, db)
        super(AnguisRedis, self).__init__()

    def __del__(self):
        super(AnguisRedis, self).__del__()
        # TODO: close the connection

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
