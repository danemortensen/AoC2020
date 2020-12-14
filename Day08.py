#!/usr/bin/env python3

import sys
import Util

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def accumulate(instructions):
    accumulator = 0
    executed = set()
    i = 0
    handlers = {
        ACC: lambda arg, acc, i: (acc + arg, i + 1),
        JMP: lambda arg, acc, i: (acc, i + arg),
        NOP: lambda arg, acc, i: (acc, i + 1),
    }
    while i < len(instructions):
        if i in executed:
            break
        executed.add(i)
        op, arg = instructions[i]
        accumulator, i = handlers[op](int(arg), accumulator, i)
    return accumulator

def main(argv):
    Util.setDay(8)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    instructions = Util.parseFile(args.filename,
        Util.regexFileHandler(r'^(acc|jmp|nop)\ \+?(-?\d+)$'))
    Util.printSolutions([
        accumulate(instructions)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
