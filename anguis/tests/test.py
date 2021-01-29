import os
from unittest import TestCase

from anguis import anguisEtcd

class Test(TestCase):

    def testEtcd(self):
        cache = anguisEtcd.AnguisEtcd()

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
