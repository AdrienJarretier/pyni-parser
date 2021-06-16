from collections.abc import Mapping, MutableMapping
import copy


class IniSectionStorage(Mapping):

    def __init__(self):
        self._storage = {}

    def __getitem__(self, property):
        return self._storage[property]

    def addValue(self, property, value):
        if property not in self:
            self._storage[property] = [value]
        else:
            self[property].append(value)

    def remove(self, a, b):
        if b in self._storage[a]:
            self._storage[a].remove(b)
            if len(self._storage[a]) == 0:
                del self._storage[a]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def encode(self):
        sectionStr = ''

        for property in self._storage:
            for val in self._storage[property]:

                sectionStr += property + '=' + str(val) + '\n'

        return sectionStr


class IniStorage(Mapping):

    def __init__(self):
        self._storage = {}

    def __getitem__(self, section):
        return self._storage[section]

    def addSection(self, sectionName):
        if sectionName not in self._storage:
            self._storage[sectionName] = IniSectionStorage()

    def __delitem__(self, a):
        del self._storage[a]

    def remove(self, a):
        self.__delitem__(a)

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def encode(self):
        iniStr = ''
        for section in self._storage:
            iniStr += '['+section+']\n'
            iniStr += self._storage[section].encode()
            iniStr += '\n'

        return iniStr

    def copy(self):
        tmp = IniStorage()
        tmp._storage = copy.deepcopy(self._storage)

        return tmp

    def mergeWith(self, otherIniStorage):
        tmpIniStorage = otherIniStorage.copy()

        # for section,properties in self:
        #     if section not in tmpIniStorage:
        #         tmpIniStorage.addSection(section)
        #     for property in properties:

        self = tmpIniStorage
