import sys
import Util

ROWS = 128
WIDTH = 8
SEATS = ROWS * WIDTH

def getSeatIds(directions):
    toId = lambda strep, zero, one: \
        int(strep.replace(zero, '0').replace(one, '1'), 2)
    return set(toId(rowStrep, 'F', 'B') * WIDTH + toId(seatStrep, 'L', 'R')
        for rowStrep, seatStrep in directions)

def partOne(seatIds):
    return max(seatIds)

def partTwo(present):
    missing = set(range(SEATS)) - present
    neighborsPresent = lambda seat: seat - 1 in present and seat + 1 in present
    return [seat for seat in missing if neighborsPresent(seat)][0]

def main(argv):
    Util.setDay(5)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    directions = Util.parseFile(args.filename,
        Util.regexFileHandler(r'^([F|B]{7})([L|R]{3})$'))
    seatIds = getSeatIds(directions)
    Util.printSolutions([partOne(seatIds), partTwo(seatIds)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
