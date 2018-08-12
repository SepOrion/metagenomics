#!/usr/bin/env python3
# Usage:gene_abundance_annot_replace.py <gene abundance_file> <annotation table>
# 根据每个样品的基因丰度，替换基因集的注释分类对应的基因，从而获得每个样品的注释信息丰度

import sys
args = sys.argv
gene_abundance = args[1]
pathway = args[2]

def my_replace():
	ab = {}
	lines = []
    
    # add to dict
	with open(gene_abundance) as F:
		for a in F:
			k = a.split()
			ab[k[0]] = k[1]

	# replace 
	with open(pathway) as pt:
		for line in pt.readlines():
			array = line.strip("\n").split("\t")
			newline = array[0]
			for value in array[1:]:
				if value in ab.keys():
					newline +="\t"+ab[value]
				else:
					continue
					#newline +="\t"+"0"
			lines.append(newline+"\n")
			#print(newline)

	# output results
	outputName = ab['Gene_ID']+"_replace.txt"
	with open(outputName,"w+") as f:
		f.writelines(lines)
my_replace()



