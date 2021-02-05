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

import bucketstore
from anguis.base import AnguisBase

class AnguisS3(AnguisBase):

    def __init__(self, bucket_name, create=False, *args, **kwargs):
        self.bucket = bucketstore.get(bucket_name, create=create)
        super(AnguisS3, self).__init__()

    def __del__(self):
        super(AnguisS3, self).__del__()

    def __getitem__(self, key):
        return self.unserialize(self.bucket.get(key))

    def __setitem__(self, key, obj):
        self.bucket.set(key, self.serialize(obj))

    def __delitem__(self, key):
        del self.bucket[key]

    def __iter__(self):
        return iter(self.bucket.list())

    def __len__(self):
        return len(self.bucket.list())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
