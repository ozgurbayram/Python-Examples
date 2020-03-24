import sys

Input = sys.argv[1]
Output = sys.argv[2]

outfile = open(Output,'w')

outfile.write(Input)
outfile.close()
