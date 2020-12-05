import sys
import Util

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
    Util.setDay(3)
    args = Util.getArgumentParser().parse_args(argv)
    hill = Util.parseFile(args.filename)
    partOne(hill)
    partTwo(hill)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
