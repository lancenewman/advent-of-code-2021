import sys

from EngineCodeReader import EngineCodeReader

if not sys.argv[1]:
    print('Usage: python3 day2.py input-file')

with open(sys.argv[1], 'r') as f:
    input = [line.strip() for line in f]
    codeReader = EngineCodeReader(input)
    print(codeReader.getPowerConsumption())
    print(codeReader.getLifeSupportRating())
