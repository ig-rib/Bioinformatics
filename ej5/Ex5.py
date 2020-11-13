import os, sys

outputFilename = "ej5-1-orfs.fasta"

if len(sys.argv) < 2:
    print("Usage: python3 Ex5.py filename [outputFilename]")
    exit(1)
filename = sys.argv[1]
if len(sys.argv) > 2:
    outputFilename = sys.argv[2]

os.system("getorf " + filename + " -outseq " + outputFilename)
os.system("sudo prosextract ./")
os.system("patmatmotifs " + filename + " -full 1  -outfile ./ej5/ej5-2.patmatmotifs")
