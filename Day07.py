import re, sys
import Util

def getRules(filename):
    parsed = Util.parseFile(filename,
        Util.regexFileHandler(r'^([a-z\ ]+)\ bags\ contain\ (.+)\.$'))
    return {p[0]: p[1] for p in parsed}

def getColorAdjacencies(rules):
    colorPattern = re.compile(r'^\d+\ ([a-z]+\ [a-z]+)\ bags?$')
    adjacencies = {}
    for color, rule in rules.items():
        if color not in adjacencies:
            adjacencies[color] = set()
        if rule == 'no other bags':
            continue
        for contents in rule.split(', '):
            match = colorPattern.match(contents)
            assert match, f'Regex did not match str: "{contents}"'
            colorContained = match.groups()[0]
            if colorContained not in adjacencies:
                adjacencies[colorContained] = set()
            adjacencies[colorContained].add(color)
    return adjacencies

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

def partOne(adjacencies):
    return len(traverseAdjacencies(adjacencies, 'shiny gold')) - 1

def main(argv):
    Util.setDay(7)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    bagRules = getRules(args.filename)
    colorAdjacencies = getColorAdjacencies(bagRules)
    print(colorAdjacencies)
    Util.printSolutions([partOne(colorAdjacencies)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
