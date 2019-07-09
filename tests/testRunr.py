import unittest
import sys,os
sys.path.append("..")
from scanner import *

class testRunr(unittest.TestCase):
    def setUp(self):
        self.scannerobj = scanner('.',ignorelist=['reports'])

    def test_1_dirbuild(self):
        filefound = False
        dir_files = self.scannerobj.build_files_set()
        for file in dir_files:
            if file == os.path.basename(__file__):
                filefound = True
        self.assertTrue(filefound,'Dir build successful')

    def test_2_scan_NOTFOUND(self):
        self.assertEqual(len(self.scannerobj.scan()),0)

    def test_3_scan_FOUND(self):
        self.scannerobj = scanner('.',['TODO1:'],['reports'])
        self.assertGreater(len(self.scannerobj.scan()),0)        

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(testRunr)])
    unittest.TextTestRunner(verbosity=2).run(suite)