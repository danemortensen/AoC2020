import re, sys
import Util

def getRules(filename):
    parsed = Util.parseFile(filename,
        Util.regexFileHandler(r'^([a-z\ ]+)\ bags\ contain\ (.+)\.$'))
    return {p[0]: p[1] for p in parsed}

def getAdjacencies(rules):
    colorPattern = re.compile(r'^(\d+)\ ([a-z]+\ [a-z]+)\ bags?$')
    forward, backward = {}, {}
    for color, rule in rules.items():
        forward[color] = []
        if color not in backward:
            backward[color] = set()
        if rule == 'no other bags':
            continue
        for contents in rule.split(', '):
            match = colorPattern.match(contents)
            assert match, f'Regex did not match str: "{contents}"'
            numContained, colorContained = match.groups()
            forward[color].append((colorContained, numContained))
            if colorContained not in backward:
                backward[colorContained] = set()
            backward[colorContained].add(color)
    return forward, backward

def traverseAdjacencies(adjacencies, start):
    visited = set([start])
    def _traverseAdjacencies(cur):
        for neighbor in adjacencies[cur]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            _traverseAdjacencies(neighbor)
    _traverseAdjacencies(start)
    return visited

def getBagsRequired(adjacencies, start):
    bagCountCache = {}
    def _getBagsRequired(cur):
        if cur in bagCountCache:
            return bagCountCache[cur]
        bagCount = 1
        for color, count in adjacencies[cur]:
            bagCount += int(count) * _getBagsRequired(color)
        bagCountCache[cur] = bagCount
        return bagCount
    return _getBagsRequired(start)

def partOne(adjacencies):
    return len(traverseAdjacencies(adjacencies, 'shiny gold')) - 1

def partTwo(adjacencies):
    return getBagsRequired(adjacencies, 'shiny gold') - 1

def main(argv):
    Util.setDay(7)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    bagRules = getRules(args.filename)
    forwardAdjacencies, backwardAdjacencies = getAdjacencies(bagRules)
    Util.printSolutions([
        partOne(backwardAdjacencies),
        partTwo(forwardAdjacencies)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
