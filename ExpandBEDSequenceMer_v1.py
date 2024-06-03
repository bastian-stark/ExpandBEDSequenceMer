filename = input('Enter file name: ')

upstream = '0'
downstream = '0'

while (int(upstream) + int(downstream) + 2) != 6:
    upstream = input('How much do you want to expand -mer upstream?: ')
    downstream = input('How much do you want to expand -mer downstream?: ')
    if (int(upstream) + int(downstream) + 2) != 6:
        print('Positions must be for hexamer')

infile = open(f"{filename}")
outfile = open(f"{filename}_expanded_upstream{upstream}.bed", "w")
for line in infile:
    line = line.strip('\n')
    line = line.split()
    line[1] = int(line[1]) - int(upstream)
    line[2] = int(line[2]) + int(downstream)
    for item in line:
        outfile.write(str(item) + '\t')
    outfile.write('\n')
