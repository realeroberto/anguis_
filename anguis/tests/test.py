import os
from unittest import TestCase

from anguis import anguisEtcd, anguisFS, anguisGit, anguisRedis, anguisSFTP

class Test(TestCase):
    def testFS(self):
        cache = anguisFS.AnguisFS(autoDestroy=True)

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

    def testEtcd(self):
        cache = anguisEtcd.AnguisEtcd()

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

    def testGit(self):
        cache = anguisGit.AnguisGit(dir='/tmp/git')

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

    def testRedis(self):
        cache = anguisRedis.AnguisRedis()

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')

    def testSFTP(self):
        hostname = os.environ['SFTP_HOSTNAME']
        username = os.environ['SFTP_USERNAME']
        password = os.environ['SFTP_PASSWORD']
        dir = os.environ['SFTP_DIR']

        cache = anguisSFTP.AnguisSFTP(hostname, username, password, dir)

        cache.set('foo', 'bar')
        print(cache.get('foo'))

        self.assertTrue(cache.get('foo') == 'bar')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
