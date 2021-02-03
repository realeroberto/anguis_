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

from sqlitedict import SqliteDict
from anguis.base import AnguisBase

class AnguisSqlite(AnguisBase):

    def __init__(self, path):
        self.sd = SqliteDict(path, autocommit=True)

    def __del__(self):
        super(AnguisSqlite, self).__del__()

    def __getitem__(self, key):
        return self.sd.__getitem__(key)

    def __setitem__(self, key, value):
        self.sd.__setitem__(key, value)

    def __delitem__(self, key):
        self.sd.__delitem__(key)

    def __iter__(self):
        return self.sd.__iter__()

    def __len__(self):
        return len(self.sd)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
