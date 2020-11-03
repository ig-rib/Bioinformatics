#!/bin/python3

## An XML parser 

import sys
from Bio.Blast import NCBIXML

if len(sys.argv) != 3:
    print("Usage: Ex4.py [path to file] [pattern]")
    exit(1)

pathToFile = sys.argv[1]
pattern = sys.argv[2]

handle = open(pathToFile)
records = list(NCBIXML.parse(handle))

descriptions = [r.descriptions for r in records]

filteredDescriptions = [
    [d for d in descs if pattern.lower() in d.title.lower()]
    for descs in descriptions
]

finalStr = ''

for (index, descs) in enumerate(filteredDescriptions):
    finalStr += f'\nResults from query "{records[index].query}" (id = {records[index].query_id}) containing pattern "{pattern}":\n\n'
    for d in descs:
        finalStr += '\tTitle: ' + d.title + '\n'
        finalStr += '\tBit-score: ' + str(d.bits) + '\n'
        finalStr += '\tRaw score: ' + str(d.score) + '\n'
        finalStr += '\te-value: ' + str(d.e) + '\n\n'

print(finalStr)