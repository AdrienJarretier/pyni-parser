import unittest

from IniParser import *


class TestIniParser(unittest.TestCase):

    def setUp(self):
        self.iniParser = IniParser()

    def testEncode(self):

        self.iniParser._storage.addSection('sect1')
        self.iniParser._storage['sect1'].addValue('a', '100')

        self.assertEqual(self.iniParser.encode(), '[sect1]\na=100\n\n')

        self.iniParser._storage['sect1'].addValue('a', 100)
        self.assertEqual(self.iniParser.encode(), '[sect1]\na=100\na=100\n\n')
        self.iniParser._storage['sect1'].addValue('b', True)
        self.assertEqual(self.iniParser.encode(),
                         '[sect1]\na=100\na=100\nb=True\n\n')

        self.iniParser._storage.addSection('sect2')
        self.iniParser._storage['sect2'].addValue('b', 'valInSec2')
        self.assertEqual(self.iniParser.encode(),
                         '[sect1]\na=100\na=100\nb=True\n\n[sect2]\nb=valInSec2\n\n')
