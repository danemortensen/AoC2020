import sys
import Util

def partOne(groupResponses):
    distinctQuestions = []
    for group in groupResponses:
        questions = set()
        for response in group:
            questions |= set(response)
        distinctQuestions.append(len(questions))
    return sum(distinctQuestions)

def partTwo(groupResponses):
    unanimousCounts = []
    for group in groupResponses:
        yesCounts = {}
        for response in group:
            for question in response:
                yesCounts[question] = yesCounts.get(question, 0) + 1
        groupSize = len(group)
        numUnanimous = sum(1 for q in yesCounts if yesCounts[q] == groupSize)
        unanimousCounts.append(numUnanimous)
    return sum(unanimousCounts)

def main(argv):
    Util.setDay(6)
    parser = Util.getArgumentParser()
    args = parser.parse_args(argv)
    groupResponses = Util.parseFile(args.filename,
        Util.groupBetweenEmptyLines(lambda g: g.split('\n')))
    Util.printSolutions([partOne(groupResponses), partTwo(groupResponses)])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
