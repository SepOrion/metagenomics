#!/usr/bin/env python3

# Usage:filter_unigenes_seq.py <fasta_file> <id_file>
# 用途：根据序列ID号，输出对应的序列

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]
id_file = sys.argv[2]
output_file = "filterSeq_"+fasta_file

# read id_file name
with open(id_file) as id_handle:
	id_name = set(line.rstrip("\n") for line in id_handle)

#read fasta_file and output
with open(fasta_file) as in_handle:
	with open(output_file,"w") as out_handle:
		for seq_record in SeqIO.parse(in_handle,"fasta"):
			if seq_record.id in id_name:
				out_handle.write(">%s\n%s\n" % (seq_record.id,seq_record.seq))


