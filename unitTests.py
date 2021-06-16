import unittest

from IniStorage import *


class TestIniSectionStorage(unittest.TestCase):

    def setUp(self):
        self.iniSectionStorage = IniSectionStorage()

    def test__getitem__(self):
        self.iniSectionStorage['b'] = 100
        self.iniSectionStorage['b'] = 2
        self.iniSectionStorage['a'] = 5
        self.assertEqual(self.iniSectionStorage['b'], [100, 2])
        self.assertEqual(self.iniSectionStorage['a'], [5])

    def test__setitem__(self):
        self.iniSectionStorage['a'] = 5
        self.assertEqual(self.iniSectionStorage, {'a': [5]})
        self.iniSectionStorage['a'] = 8
        self.assertEqual(self.iniSectionStorage, {'a': [5, 8]})

    def testremove(self):
        self.iniSectionStorage['a'] = 5
        self.iniSectionStorage['a'] = 8
        self.iniSectionStorage.remove('a', 5)
        self.assertEqual(self.iniSectionStorage, {'a': [8]})
        self.iniSectionStorage.remove('a', 8)
        self.assertEqual(self.iniSectionStorage, {})

    def test__len__(self):
        self.iniSectionStorage['b'] = 100
        self.iniSectionStorage['b'] = 2
        self.iniSectionStorage['a'] = 5
        self.assertEqual(len(self.iniSectionStorage), 2)


unittest.main(verbosity=2)
