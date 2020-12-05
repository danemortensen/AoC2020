import re, sys
import Util

def getPassports(filename):
    passports = []
    with open(filename, 'r') as f:
        passport = ''
        for line in f:
            line = line.strip()
            if not line:
                passports.append(passport)
                passport = ''
            else:
                passport += ' ' + line
        passport.replace('\n', ' ')
        passports.append(passport)
    return passports

def getFields(passports):
    fieldDicts = []
    for passport in passports:
        fields = {}
        for datum in passport.split():
            pair = datum.split(':')
            fields[pair[0]] = pair[1]
        fieldDicts.append(fields)
    return fieldDicts

def parseInput(filename):
    return getFields(getPassports(filename))

def filterMissingFields(fieldDicts):
    requiredFields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return [d for d in fieldDicts if not requiredFields - set(d.keys())]

def filterInvalidFields(fieldDicts):
    betweenHandler = lambda low, high: lambda s: len(s) == 4 and low <= int(s) <= high
    regexHandler = lambda pattern: lambda s: re.match(pattern, s)

    def _hgtHandler(s):
        match = re.match(r'(\d+)(cm|in)', s)
        if not match:
            return False
        units, metric = match.groups()
        low, high = (150, 193) if metric == 'cm' else (59, 76)
        return low <= int(units) <= high

    handlers = {
        'byr': betweenHandler(1920, 2002),
        'iyr': betweenHandler(2010, 2020),
        'eyr': betweenHandler(2020, 2030),
        'hgt': _hgtHandler,
        'hcl': regexHandler(r'^#[0-9|a-f]{6}$'),
        'ecl': regexHandler(r'^amb|blu|brn|gry|grn|hzl|oth$'),
        'pid': regexHandler(r'^\d{9}$'),
        'cid': lambda s: True
    }

    validated = []
    for fields in fieldDicts:
        valid = True
        for k, v in fields.items():
            if not handlers[k](v):
                valid = False
                break
        if valid:
            validated.append(fields)
    return validated

def main(argv):
    Util.setDay(4)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    fieldDicts = parseInput(args.filename)
    withRequired = filterMissingFields(fieldDicts)
    print(f'Part 1: {len(withRequired)}')
    validated = filterInvalidFields(withRequired)
    print(f'Part 2: {len(validated)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
