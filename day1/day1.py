import sys

from Fathometer import Fathometer

if not sys.argv[1]:
    print('Usage: python3 day1.py input-file')

with open(sys.argv[1], 'r') as f:
    input = [int(line.rstrip()) for line in f]
    fathometer = Fathometer(input)
    print(f'Part 1: {fathometer.countIncreases()}')
    print(f'Part 2: {fathometer.countSlidingWindowIncreases(3)}')
