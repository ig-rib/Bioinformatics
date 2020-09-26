#!/bin/python3

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import translate
from Bio.SeqRecord import SeqRecord
from utils import translatemRNASequence

with open("ej1/sirt6.gb", "rU") as input_handle:
    with open("ej1/sirt6.fasta", "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "genbank")
        # for sequence in sequences:
        #     print(sequence.translate())
        # translatedSequences = list(map(lambda x: x.translate(), sequences))
        # count = SeqIO.write(translatedSequences, output_handle, "fasta")
        for seq in sequences:
            translatemRNASequence(seq, "ej1/sirt6.fasta")

# print("Converted %i records" % count)

