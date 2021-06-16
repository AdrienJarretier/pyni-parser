from collections.abc import Mapping, MutableMapping


class IniSectionStorage(Mapping):

    def __init__(self):
        self._storage = {}

    def __getitem__(self, property):
        return self._storage[property]

    def __setitem__(self, a, b):
        if a not in self._storage:
            self._storage[a] = [b]
        else:
            self._storage[a].append(b)

    def remove(self, a, b):
        if b in self._storage[a]:
            self._storage[a].remove(b)
            if len(self._storage[a]) == 0:
                del self._storage[a]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)


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

