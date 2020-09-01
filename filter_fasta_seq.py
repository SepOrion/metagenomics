#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description="Used to filter sequences by length")
parser.add_argument("-i","--intput",dest="Intput_file",metavar="",help="Input fasta file")
parser.add_argument("-o","--Output",dest="Output_file",metavar="",help="Output file name")
parser.add_argument("-l","--Length",dest="filterLength",metavar="",default=500,type = int,help="Length of seq,(default 500)")
args = parser.parse_args()

seq={}
with open(args.Intput_file) as fa:
	for line in fa:
		if line.startswith(">"):
			seq_name = line.split()[0]
			seq[seq_name] = ''
		else:
			seq[seq_name]+=line.replace('\n', '')

#按序列长度筛选
with open(args.Output_file,"w") as f:
    for key,value in seq.items():
        if len(value) >= args.filterLength:
            f.write(key+"\n")
            f.write(value+"\n")