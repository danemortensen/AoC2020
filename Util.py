import argparse, collections, re

def setDay(d):
    global day
    day = str(d).zfill(2)

def getDay():
    assert day, 'Day has not been set yet. Please run setDay.'
    return day

def getArgumentParser(filename=True):
    parser = argparse.ArgumentParser(
        description=f'Day {getDay()} of Advent of Code 2020')
    if filename:
        parser.add_argument('filename', help='input filename')
    return parser

def groupBetweenEmptyLines(groupHandler=None):
    def _groupBetweenEmptyLines(f):
        parsed = re.split(r'(?:\r?\n){2,}', f.read().strip())
        if groupHandler:
            parsed = [groupHandler(group) for group in parsed]
        return parsed
    return _groupBetweenEmptyLines

def regexFileHandler(regex):
    pattern = re.compile(regex)
    def _regexFileHandler(f):
        parsed = []
        for line in f:
            match = pattern.match(line)
            assert match, f'Line "{line}" does not match regex {regex}'
            parsed.append(match.groups())
        return parsed
    return _regexFileHandler

def intFileHandler(f):
    return [int(line) for line in f]

def parseFile(filename, handler):
    with open(filename, 'r') as f:
        if not handler:
            return [line.strip() for line in f]
        return handler(f)

def printSolutions(solutions):
    print()
    print('===================')
    print('ADVENT OF CODE 2020')
    print(f'Day {getDay()}')
    print('===================')
    print()
    for i in range(len(solutions)):
        print(f'  Part {i + 1}: {solutions[i]}')
        print()

class LruSet(object):
    def __init__(self, capacity):
        self.__capacity = capacity
        self._size = 0
        self._counts = {}
        self._queue = collections.deque()

    def values(self):
        return list(self._queue)

    def add(self, val):
        lru = None
        if self._size == self.__capacity:
            lru = self._queue.popleft()
            self._counts[lru] -= 1
            if self._counts[lru] == 0:
                del self._counts[lru]
            self._size -= 1
        self._queue.append(val)
        self._counts[val] = self._counts.get(val, 0) + 1
        self._size += 1
        return lru

    def __str__(self):
        return 'LruCache([' + ', '.join(str(v) for v in self._queue) + '])'
