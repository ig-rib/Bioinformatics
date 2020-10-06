from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio import SeqIO
import sys
import os

if len(sys.argv) != 2 and len(sys.argv) != 4:
    print("Usage: python3 Ex2.py fastaFilePath [-local -dbpath=pathToLocalDb]")
else:
    fileName = sys.argv[1]
    local = False
    if len(sys.argv) > 2:
        local = sys.argv[2] == "-local"
    if local:
        dbpath = sys.argv[3].split("=").pop().strip()
    with open(fileName, "r") as input_handle:
        sequences = SeqIO.parse(input_handle, "fasta")
        i = 0
        for seq in sequences:
            i += 1
            if local:
                blast_cmd = NcbiblastpCommandline(query=fileName, db=dbpath, out=f"ej2/blast-seq{i}-local.out")
                os.system(str(blast_cmd))
            else:                
                result_handle = NCBIWWW.qblast("blastp", "swissprot", seq.format("fasta"))
                with open(f"blast-seq{i}-web.out", "w") as output_handle:
                    output_handle.write(result_handle.read())
