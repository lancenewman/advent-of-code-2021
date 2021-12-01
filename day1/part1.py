
def countIncreases(fileName: str):
    with open(fileName, 'r') as inputFile:
        prevDepth = None
        increases = 0
        for line in inputFile:
            currentDepth = int(line.rstrip())
            if prevDepth and currentDepth > prevDepth:
                increases += 1
            prevDepth = currentDepth
        return increases


if __name__ == '__main__':
    print(countIncreases('part1-input.txt'))
