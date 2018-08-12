#!/usr/bin/env python
# Usage:find_kegg_in_species.py <keggFile> <speciesFile>
# keggFile : from interested in kegg pathway
# speciesFile : species abundance table

import os
import sys

args = sys.argv

keggFile = args[1]
speciesFile = args[2]

lines = []
kg_lines = []

with open(keggFile) as kg:
	for line in kg.readlines():
		k1 = line.strip("\n").split("\t")
		for value in k1:
			k11 = value +"_1"
			kg_lines.append(k11)

with open(speciesFile) as sp:
	for line in sp.readlines():
		k2 = line.strip("\n").split("\t")
		newline = k2[0]
		for values in k2[1:]:
			if values in kg_lines:
				#newline = k2[0]
				newline +="\t" + values
			else:
				continue
		lines.append(newline+"\n")

if not os.path.exists("keggGene_in_species_table.txt"):
	with open("keggGene_in_species_table.txt","w+") as f:
		f.writelines(lines)
else:
	print("File already exists,remove it and try once again!")
