#！/usr/bin/env python3

import argparse
from Bio import SeqIO

def get_args():
	parser = argparse.ArgumentParser(description="用途：根据序列长度过滤MetaGeneMark预测的genes序列，并根据文件名修改序列ID号")
	parser.add_argument("-i",dest="fastaFile",metavar="",help="输入文件：MetaGeneMark预测的genes序列")
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
