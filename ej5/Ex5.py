import os, sys

outputFilename = "orfs.fasta"

if len(sys.argv) < 2:
    print("Usage: python3 Ex5.py filename [outputFilename]")
    exit(1)
filename = sys.argv[1]

if len(sys.argv) > 2:
    outputFilename = sys.argv[2]

os.system("getorf " + filename + " -outseq " + outputFilename)