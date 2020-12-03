import argparse
import sys

def parseInput(filename):
    with open(filename) as f:
        return [int(line) for line in f]

def twoSum(nums, sum_, start=0):
    seen = set()
    for num in nums[start:]:
        complement = sum_ - num
        if complement in seen:
            return num, complement
        else:
            seen.add(num)
    return None, None

def threeSum(nums, sum_):
    for i in range(len(nums) - 2):
        a = nums[i]
        complement = sum_ - a
        b, c = twoSum(nums, complement, i + 1)
        if b and c:
            break
    return a, b, c

def partOne(nums, sum_):
    a, b = twoSum(nums, sum_)
    assert a and b, f'Could not find two numbers that add to {sum_}'
    return a * b

def partTwo(nums, sum_):
    a, b, c = threeSum(nums, sum_)
    assert all([a, b, c]), f'Could not find three numbers that add to {sum_}'
    return a * b * c

def main(argv):
    parser = argparse.ArgumentParser(description='Day 1 of Advent of Code 2020')
    parser.add_argument('filename', help='input filename')
    parser.add_argument('-s', '--sum', type=int, default=2020,
        help='what our targets should add to')
    args = parser.parse_args(argv)

    nums = parseInput(args.filename)
    sum_ = args.sum
    partOneSolution = partOne(nums, sum_)
    partTwoSolution = partTwo(nums, sum_)

    print(f'Part 1: {partOneSolution}')
    print(f'Part 2: {partTwoSolution}')

if __name__ == '__main__':
    main(sys.argv[1:])
