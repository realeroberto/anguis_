from unittest import TestCase

from anguis import anguisFS, anguisGit

class Test(TestCase):
    def testFS(self):
        cache = anguisFS.AnguisFS(autoDestroy=True)

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

    def testGit(self):
        cache = anguisGit.AnguisGit(dir='/tmp/git')

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
