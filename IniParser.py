from IniStorage import *

class IniParser():

    def __init__(self):
        self._storage = IniStorage()

    def _parseLine(self, line):
        print(line)
        if line.startswith('['):
            print('section')
        else:
            print('option')

    # parse entire string from an ini file
    def parseString(self, s):
        i = 0
        for l in s.split():
            self._parseLine(l)
            i += 1

    def parseFile(self, filename):

        with open(filename) as f:
            self.parseString(f.read())


parser = IniParser()

parser.parseFile('test/0-readAndOutput/input.ini')
