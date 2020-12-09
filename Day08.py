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
    def _handleAcc(arg):
        nonlocal accumulator, i
        accumulator += arg
        i += 1
    def _handleJmp(arg):
        nonlocal i
        i += arg
    def _handleNop(arg):
        nonlocal i
        i += 1
    handlers = {
        ACC: _handleAcc,
        JMP: _handleJmp,
        NOP: _handleNop
    }
    while i < len(instructions):
        if i in executed:
            break
        executed.add(i)
        op, arg = instructions[i]
        handlers[op](int(arg))
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
