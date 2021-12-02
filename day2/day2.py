import sys

from Submarine import Submarine

if not sys.argv[1]:
    print('Usage: python3 day2.py input-file')

with open(sys.argv[1], 'r') as f:
    input = [line.rstrip() for line in f]
    submarine = Submarine(input)
    submarine.move()
    product = submarine.horizontal * submarine.depth
    print(f'Day 2 Part 1: {product}')

    submarine.reset()
    submarine.moveWithAim()
    product = submarine.horizontal * submarine.depth
    print(f'Day 2 Part 2: {product}')
