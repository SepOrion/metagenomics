#！/usr/bin/env python3

import argparse
from Bio import SeqIO

def get_args():
	parser = argparse.ArgumentParser(description="用途：用于过滤fasta序列")
	parser.add_argument("-i",dest="fastaFile",metavar="",help="输入文件：fasta格式")
	parser.add_argument("-l",dest="cutoff",metavar="",type=int,help="要保留的序列长度")
	parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
	return parser.parse_args()
args = get_args()

newId =  args.fastaFile.split(".")[0]

with open(args.fastaFile) as handle:
	cleanSeq = []
	for record in SeqIO.parse(handle,"fasta"):
		if len(record.seq)>=args.cutoff:
			record.id=newId+"_"+record.id.split("|")[0]
			record.description=''
			cleanSeq.append(record)
SeqIO.write(cleanSeq,args.outFile,"fasta")
