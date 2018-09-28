#!/usr/bin/env python3

import argparse
from Bio import SeqIO

def get_args():
	parser = argparse.ArgumentParser(description="用途：按序列数目拆分fasta文件")
	parser.add_argument("-i",dest="fastaFile",metavar="",help="输入文件名")
	parser.add_argument("-n",dest="fileNum",metavar="",help="每个文件包含的序列数目",type=int)
	return parser.parse_args()
args = get_args()

def batch_iterator(iterator,batch_size):
	entry = True
	while entry:
		batch = []
		while len(batch) < batch_size:
			try:
				entry = next(iterator)
			except StopIteration:
				entry = None
			if entry is None:
				break
			batch.append(entry)
		if batch:
			yield batch
"""
# 按生成的文件数进行拆分
seqNum = 0
for rec in SeqIO.parse(args.fastaFile,"fastq"):
	seqNum +=1
seqCount = int(seqNum/args.fileNum)
"""
record_iter = SeqIO.parse(args.fastaFile,"fastq")
for i,batch in enumerate(batch_iterator(record_iter,args.fileNum)):
	filename = args.fastaFile+"_%i" % (i+1)
	with open(filename,"w") as handle:
		count = SeqIO.write(batch,handle,"fastq")
	print("Wrote %i records to %s" % (count,filename))

