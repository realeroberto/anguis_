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
import shutil
from anguis.base import AnguisBase

class AnguisFS(AnguisBase):

    def _key_to_path(self, key):
        return os.path.join(self.dir, key)

    def __init__(self, dir=None, autoDestroy=True):
        if not dir:
            import tempfile
            dir = tempfile.mkdtemp()
        self.dir = dir
        self.autoDestroy = autoDestroy
        super(AnguisFS, self).__init__()

    def __del__(self):
        super(AnguisFS, self).__del__()
        if self.autoDestroy:
            shutil.rmtree(self.dir)

    def __getitem__(self, key):
        try:
            with open(self._key_to_path(key), "r") as h:
                return h.readline()
        except FileNotFoundError:
            return None

    def __setitem__(self, key, value):
        path = self._key_to_path(key)
        with open(path, "w") as h:
            h.write("%s" % value)

    def __delitem__(self, key):
        return os.remove(self._key_to_path(key))

    def __iter__(self):
        return iter(os.listdir(self.dir))

    def __len__(self):
        return len(os.listdir(self.dir))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
