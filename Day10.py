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
    return freqs[1] * freqs[3]

def getJoltageTree(joltages):
    joltageTree = {}
    joltages.sort()
    joltages.insert(0, 0)
    joltages.append(joltages[-1] + 3)
    for i, joltage in enumerate(joltages):
        joltageTree[joltage] = []
        for j in joltages[i + 1:i + 4]:
            if j > joltage + 3:
                break
            joltageTree[joltage].append(j)
    return joltageTree

def countValidAdapterChains(joltageTree):
    counts = {}
    def _count(root):
        nonlocal joltageTree, counts
        if root not in counts:
            if not joltageTree[root]:
                return 1
            counts[root] = sum(_count(j) for j in joltageTree[root])
        return counts[root]
    return _count(0)

def partTwo(adapters):
    return countValidAdapterChains(getJoltageTree(adapters))

def main(argv):
    Util.setDay(10)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    adapters = Util.parseFile(args.filename, Util.intFileHandler)
    Util.printSolutions([partOne(adapters), partTwo(adapters)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
