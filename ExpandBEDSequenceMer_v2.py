#ExpandedBEDSequenceMer V2
#Bastian Stark
#May 31, 2024
#Short script for expanding the upstream and downstream positions of a dinucleotide from BED file. Only designed for hexamers.

filename = input('Enter file name: ')

upstream = '0'
downstream = '0'

#While loop to exsure upstream and downstream expansion parameters form a hexamer
while (int(upstream) + int(downstream) + 2) != 6:
    upstream = input('How much do you want to expand -mer upstream?: ')
    downstream = input('How much do you want to expand -mer downstream?: ')
    if (int(upstream) + int(downstream) + 2) != 6:
        print('Positions must be for hexamer')


infile = open(f"{filename}.bed")
outfile = open(f"{filename}_expanded_upstream{upstream}.bed", "w")
for line in infile:
    line = line.strip('\n')
    line = line.split()
    #adjust positions for + strand
    if line[5] == "+":
        line[1] = int(line[1]) - int(upstream)
        line[2] = int(line[2]) + int(downstream)
    #adjust positions for - strand; opposite orientation, so calculated differently
    elif line[5] == "-":
        line[1] = int(line[1]) - int(upstream) - int(downstream) + int(upstream)
        line[2] = int(line[2]) - int(downstream) - int(downstream) + int(upstream)
    else:
        print('Detected strand with neither + nor - orientation; skipping')
    for item in line:
        outfile.write(str(item) + '\t')
    outfile.write('\n')