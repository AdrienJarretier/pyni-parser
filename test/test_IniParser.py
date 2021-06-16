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

    def testparseFile(self):

        INPUT_FILE = 'test/0-readAndOutput/input.ini'

        self.iniParser.parseFile(INPUT_FILE)

        parsedContentEncoded = self.iniParser.encode()
        rawInputContent = ''
        with open(INPUT_FILE) as inF:
            rawInputContent = inF.read()

        parsedContentEncoded = parsedContentEncoded.strip('\n')
        rawInputContent = rawInputContent.strip('\n')

        self.assertEqual(parsedContentEncoded, rawInputContent)

    def testwriteFile(self):

        INPUT_FILE = 'test/0-readAndOutput/input.ini'
        OUTPUT_FILE = 'test/0-readAndOutput/output.ini'

        self.iniParser.parseFile(INPUT_FILE)
        self.iniParser.writeFile(OUTPUT_FILE)

        rawInputContent = ''
        rawOutputContent = ''
        with open(INPUT_FILE) as inF:
            rawInputContent = inF.read()

        with open(OUTPUT_FILE) as outF:
            rawOutputContent = outF.read()

        rawInputContent = rawInputContent.strip('\n')
        rawOutputContent = rawOutputContent.strip('\n')

        self.assertEqual(rawInputContent, rawOutputContent)
