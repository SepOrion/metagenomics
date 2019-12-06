#!/usr/bin/env python3

import gzip
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description="用途：统计双端fastq序列文件reads数、数据量、平均长度、q30比例、GC含量")
parser.add_argument("-i",dest="read1",metavar="",help="read1文件")
parser.add_argument("-ii",dest="read2",metavar="",help="read2文件")
args = parser.parse_args()

# read fq file
def quality_stat(Fq): 
    with gzip.open(Fq,'rt') as fq:
        gc = 0 ; baseNums = 0 ; q30 = 0
        readNums = 0 ; length = []
        for rec in SeqIO.parse(fq,'fastq'):
            gc += rec.seq.count("G") + rec.seq.count("C")
            baseNums += len(rec.seq)
            length.append(len(rec.seq))
            readNums += 1
            q30 += sum(x >=30 for x in rec.letter_annotations["phred_quality"])
            ave_length = sum(length)/len(length)
        return readNums,baseNums,ave_length,q30,gc 

fq1 = quality_stat(args.read1)
fq2 = quality_stat(args.read2)

readNums = fq1[0] #reads数
totalBase = fq1[1] + fq2[1] #总碱基数
Ave_length = int((fq1[2] + fq2[2])/2) # 平均长度
Q30 =fq1[3] + fq2[3]  # q30
GC = fq1[4] + fq2[4]   # GC含量

name = args.read1
        
print(name,end='\t') # 样品名
print(readNums,end='\t') # 总reads数目
print(totalBase/1000000,end='\t') # 碱基数目（单位：百万)
print(Ave_length,end='\t')  # 平均长度
print('%.2f' % (Q30/totalBase*100),end='\t') # q30比例%
print('%.2f' % (GC/totalBase*100)) # GC含量

