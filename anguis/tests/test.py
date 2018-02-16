from unittest import TestCase

from anguis import anguisFS

class Test(TestCase):
    def test(self):
        cache = anguisFS.AnguisFS(autoDestroy=True)

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
