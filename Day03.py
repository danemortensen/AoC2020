import argparse, re, sys

def parseInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def countTrees(hill, dx, dy):
    trees = 0
    width = len(hill[0])
    x = 0
    for y in range(0, len(hill), dy):
        if hill[y][x % width] == '#':
            trees += 1
        x += dx
    return trees

def partOne(hill):
    print(f'Part 1: {countTrees(hill, 3, 1)}')

def partTwo(hill):
    product = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for dx, dy in slopes:
        product *= countTrees(hill, dx, dy)
    print(f'Part 2: {product}')

def main(argv):
    parser = argparse.ArgumentParser(description='Day 3 of Advent of Code 2020')
    parser.add_argument('filename', help='input filename')
    args = parser.parse_args(argv)
    hill = parseInput(args.filename)
    partOne(hill)
    partTwo(hill)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
