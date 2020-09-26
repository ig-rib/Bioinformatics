#!/bin/python3

from Bio.Blast import NCBIWWW
from Bio import SeqIO
import sys

if len(sys.argv) != 2:
    print("Usage: python3 Ex2.py [fastaFilePath]")
else:
    fileName = sys.argv[1]
    with open(fileName, "r") as input_handle:
        sequences = SeqIO.parse(input_handle, "fasta")
        i = 0
        for seq in sequences:
            i += 1
            print(seq)
            result_handle = NCBIWWW.qblast("blastp", "swissprot", seq.format("fasta"))
            with open(f"blast-seq{i}.out", "w") as output_handle:
                output_handle.write(result_handle.read())
            