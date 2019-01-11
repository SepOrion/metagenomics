#!/usr/bin/env python3

import argparse
from Bio import SeqIO
parser = argparse.ArgumentParser(description=
								 "用途：根据序列ID号，输出对应的序列。\n"
								"Usage:find_seq_by_id.py -i genes.fa -id id.txt -o genes_clean.fa",formatter_class = ap.RawTextHelpFormatter)
parser.add_argument("-i",dest="fasta",metavar="",help="fasta序列文件，例如去冗余后的基因集")
parser.add_argument("-id",dest="Id",metavar="",help="需要查询的序列ID，格式：一行一个ID号")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

# read id_file name
with open(args.Id) as id_handle:
	id_name = set(line.rstrip("\n") for line in id_handle)

#read fasta_file and output
with open(args.fasta) as in_handle:
	with open(args.outFile,"w") as out_handle:
		for seq_record in SeqIO.parse(in_handle,"fasta"):
			if seq_record.id in id_name:
				out_handle.write(">%s\n%s\n" % (seq_record.id,seq_record.seq))


