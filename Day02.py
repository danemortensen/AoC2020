import sys
import Util

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
    Util.setDay(2)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    passwords = Util.parseFile(args.filename,
        Util.regexFileHandler(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$'))
    partOne(passwords)
    partTwo(passwords)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
