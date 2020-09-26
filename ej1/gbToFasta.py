#!/bin/python3

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import translate
from Bio.SeqRecord import SeqRecord
from utils import translatemRNASequence
import sys

if len(sys.argv) != 2:
    print("Usage: gbToFasta [genBankFilePath]")
else:
    genBankFilePath = sys.argv[1]
    outputFilePathSplit = genBankFilePath.split('.')
    if outputFilePathSplit[-1] in ("gb", "gbk"):
        outputFilePathSplit.pop()
    outputFilePath = ".".join(outputFilePathSplit)

    with open(genBankFilePath, "rU") as input_handle:
        sequences = SeqIO.parse(input_handle, "genbank")
        # for sequence in sequences:
        #     print(sequence.translate())
        # translatedSequences = list(map(lambda x: x.translate(), sequences))
        # count = SeqIO.write(translatedSequences, output_handle, "fasta")
        i = 0
        for seq in sequences:
            i += 1
            translatemRNASequence(seq, outputFilePath + f"-seq{i}.fasta")

    # print("Converted %i records" % count)

