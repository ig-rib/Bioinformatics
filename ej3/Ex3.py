#!/bin/python3
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio import AlignIO
import sys

arabidopsisSir1Seq = SeqIO.parse("ej3/arabidopsis-sir1.fasta", "fasta")
mouseSir6Seq = SeqIO.parse("ej3/mouse-sir6.fasta", "fasta")
fruitFlySir6Seq = SeqIO.parse("ej3/fruit-fly-sir6.fasta", "fasta")

