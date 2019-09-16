#!/usr/share/python3
# recap.py
# date:16.9.2019

import csv
import sys
import statistics

file_name = sys.argv[1]
data = []
pos = []
neg = []

with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            e = e.strip()
            data.append(int(e))

    print(data)

_sum = sum(data)
_max = max(data)
_min = min(data)

print(f'Maximum number is {_max} .')
print(f'Minimum number is {_min} .')
print(f'Sum of values is {_sum} .')

pos = [e for e in data if e > 0]
neg = [e for e in data if e < 0]

print(pos)
print(neg)
