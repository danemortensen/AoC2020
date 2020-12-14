#!/usr/bin/env python3

import sys
import Util

class TwoSumLruSet(Util.LruSet):
    def hasTwoSum(self, sum_):
        complements = set()
        for num in self._queue:
            if num in complements:
                return True
            complements.add(sum_ - num)
        return False

def firstNonSum(encrypted):
    cache = TwoSumLruSet(25)
    preamble = encrypted[:25]
    for num in preamble:
        cache.add(num)
    payload = encrypted[25:]
    for num in payload:
        if not cache.hasTwoSum(num):
            return num
        cache.add(num)
    return None

def sumRange(nums, sum_):
    sums = {}
    for i in range(len(nums)):
        sums[i] = 0
        num = nums[i]
        toDelete = []
        for j in sums:
            sums[j] += num
            if sums[j] == sum_:
                return nums[j:i + 1]
            if sums[j] >= sum_:
                toDelete.append(j)
        for key in toDelete:
            del sums[key]
    return None

def sumOfMinAndMax(nums):
    return min(nums) + max(nums)

def main(argv):
    Util.setDay(9)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    encrypted = Util.parseFile(args.filename, Util.intFileHandler)
    solution1 = firstNonSum(encrypted)
    solution2 = sumOfMinAndMax(sumRange(encrypted, solution1))
    Util.printSolutions([solution1, solution2])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
