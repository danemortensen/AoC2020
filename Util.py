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

def parseFile(filename, regex=None):
    parsed = []
    if regex:
        pattern = re.compile(regex)
    with open(filename) as f:
        for line in f:
            if regex:
                match = pattern.match(line)
                assert match, f'Line "{line}" does not match regex {regex}'
                parsed.append(match.groups())
            else:
                parsed.append(line.strip())
    return parsed

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
