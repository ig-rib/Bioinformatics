#!/bin/python3

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import translate
from Bio.SeqRecord import SeqRecord

def translatemRNASequence(seq, filename="output", translationTable=1):

    allPossibilities = []

    for frame in range(3):
        trans = seq[frame:].translate(to_stop=True)
        reverse = seq[::-1][frame:].translate(to_stop=True)
        allPossibilities.append(trans)
        allPossibilities.append(reverse)

    i = 0
    for protein in allPossibilities:
        i = i + 1
        # currentProtein = Seq(protein)

        # currentProteinRecord = SeqRecord(protein, name=seq.name)
        protein.id = seq.id + "." + str(i) + " -> Generated Protein;"
        protein.description = seq.description + "; frame " + str(i)
        # with open(filename, "w") as output_handle:
        #     SeqIO.write(protein, output_handle, "fasta")
    with open(filename, "w") as output_handle:
        SeqIO.write(allPossibilities, output_handle, "fasta")      