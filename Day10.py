#!/usr/bin/env python3

import sys
import Util

def deltaFreqs(adapters):
    adapters.sort()
    # Treat charging outlet as 0 jolts
    inputJoltage = 0
    deltaFreqs = [None, 0, 0, 0]
    for outputJoltage in adapters:
        delta = outputJoltage - inputJoltage
        deltaFreqs[delta] += 1
        inputJoltage = outputJoltage
    # Device adapter is rated for max(adapters) + 3 jolts
    deltaFreqs[3] += 1
    return deltaFreqs

def partOne(adapters):
    freqs = deltaFreqs(adapters)
    return deltaFreqs[1] * deltaFreqs[3]

def main(argv):
    Util.setDay(10)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    adapters = Util.parseFile(args.filename, Util.intFileHandler)
    freqs = deltaFreqs(adapters)
    Util.printSolutions([partOne(adapters)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
