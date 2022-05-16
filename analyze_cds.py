'''
This program accepts the protein coding regions of any organism as an infile, and prints to the console its GC content.
This code can be used on any CDS file.
'''


import re

infile = open("ecoli_cds.fna", "r")

sequences_total = ""
for line in infile:
    if ">" not in line:
        sequences_total += line
    else:
        pass


g_content = sequences_total.count("G")
c_content = sequences_total.count("C")

total_chars = len(sequences_total)

gc_content = round((g_content + c_content) / total_chars, 2)

print("The GC content of E.coli is:", gc_content)




