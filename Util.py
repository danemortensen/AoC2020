import argparse, re

def getArgumentParser(day, filename=True):
    parser = argparse.ArgumentParser(
        description=f'Day {day} of Advent of Code 2020')
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
