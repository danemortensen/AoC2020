import argparse, re, sys

def parseInput(filename):
    passwords = []
    PATTERN = r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$'
    pattern = re.compile(PATTERN)
    with open(filename) as f:
        for line in f:
            match = pattern.match(line)
            assert match
            passwords.append(match.groups())
    return passwords

def charFreqInBounds(low, high, char, pwd):
    return int(low) <= sum(1 if c is char else 0 for c in pwd) <= int(high)

def charAtOnePos(a, b, char, pwd):
    charIsAt = lambda pos: pos <= len(pwd) and pwd[pos - 1] is char
    return sum([charIsAt(int(a)), charIsAt(int(b))]) == 1

def numValid(validator, passwords):
    return sum(validator(*password) for password in passwords)

def partOne(passwords):
    print(f'Part 1: {numValid(charFreqInBounds, passwords)}')

def partTwo(passwords):
    print(f'Part 2: {numValid(charAtOnePos, passwords)}')

def main(argv):
    parser = argparse.ArgumentParser(description='Day 2 of Advent of Code 2020')
    parser.add_argument('filename', help='input filename')
    args = parser.parse_args(argv)
    passwords = parseInput(args.filename)
    partOne(passwords)
    partTwo(passwords)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
