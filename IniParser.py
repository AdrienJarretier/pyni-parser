from IniStorage import *


class IniParser():

    def __init__(self):
        self._storage = IniStorage()

    def _parseLine(self, line):
        if line.startswith('['):
            return [line[1:-1]]
        else:
            return line.split('=')

    # parse entire string from an ini file
    def parseString(self, s):
        currentSection = None
        for l in s.split():
            parsedLine = self._parseLine(l)
            if(len(parsedLine) == 1):
                self._storage.addSection(parsedLine[0])
                currentSection = self._storage[parsedLine[0]]
            else:
                currentSection.addValue(parsedLine[0], parsedLine[1])

    def parseFile(self, filename):

        with open(filename) as f:
            self.parseString(f.read())

    def encode(self):

        return self._storage.encode()

    def writeFile(self, filename):

        with open(filename, 'w') as f:
            f.write(self.encode())

    # def _mergeIntoString(self, string):

    # def _mergeIntoFile(self, filename):

    #     targetFileParser = IniParser()
    #     targetFileParser.parseFile(filename)
    #     self._storage.mergeInto

    # def mergeInto

    def mergeWith(self, filename):

        targetFileParser = IniParser()
        targetFileParser.parseFile(filename)

        self._storage.mergeWith(targetFileParser._storage)


def test1_merge():
    parser = IniParser()
    parser.parseFile('test/1-merge/testi.ini')
    parser.mergeWith('test/1-merge/testo.ini')
    parser.writeFile('test/1-merge/testo.ini')


