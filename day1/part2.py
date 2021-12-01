def countSlidingIncreases(fileName: str):
    with open(fileName, 'r') as f:
        input = [int(line.rstrip()) for line in f.readlines()]
        increases = 0
        if len(input) < 3:
            # Not long enough for any sliding windows
            return increases

        prevWindow = None
        for i in range(len(input)):
            if i + 3 <= len(input):
                currentWindow = sum(input[i:i+3])
            if prevWindow and currentWindow > prevWindow:
                increases += 1

            prevWindow = currentWindow
    return increases


if __name__ == '__main__':
    print(countSlidingIncreases('input.txt'))
