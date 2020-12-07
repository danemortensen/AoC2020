import argparse, re

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
