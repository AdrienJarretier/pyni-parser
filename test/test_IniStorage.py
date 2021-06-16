
import unittest

from IniStorage import *


class TestIniStorage(unittest.TestCase):

    def setUp(self):
        self.iniStorage = IniStorage()

    def test__getitem__(self):
        self.iniStorage.addSection('testSection')
        self.iniStorage.addSection('testSection2')
        self.assertEqual(self.iniStorage['testSection'], IniStorage())
        self.assertEqual(self.iniStorage['testSection'], {})
        self.assertEqual(self.iniStorage['testSection2'], {})
        self.iniStorage['testSection']['a'] = 2
        self.assertIn('a', self.iniStorage['testSection'])
        self.assertSequenceEqual(self.iniStorage['testSection']['a'], [2])

    def testaddSection(self):
        self.iniStorage.addSection('testSection')
        self.iniStorage.addSection('testSection2')
        self.assertEqual(self.iniStorage.keys(), {
                         'testSection': '', 'testSection2': ''}.keys())
        self.assertEqual(self.iniStorage, {
                         'testSection': {}, 'testSection2': {}})

    def test__delitem__(self):
        self.iniStorage.addSection('sec1')
        self.iniStorage['sec1']['a'] = 2
        del self.iniStorage['sec1']
        self.assertEqual(self.iniStorage, {})


    def testremove(self):
        self.iniStorage.addSection('sec1')
        self.iniStorage['sec1']['a'] = 2
        self.iniStorage.remove('sec1')
        self.assertEqual(self.iniStorage, {})

    def test__len__(self):
        self.assertEqual(len(self.iniStorage), 0)
        self.iniStorage.addSection('sec1')
        self.assertEqual(len(self.iniStorage), 1)
        self.iniStorage.addSection('sec2')
        self.assertEqual(len(self.iniStorage), 2)


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
