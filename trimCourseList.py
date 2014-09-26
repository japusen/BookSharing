import sys

inputfile = str(sys.argv[1])
course = str(sys.argv[2])
output = open(course + ".txt",'w')

if(len(sys.argv)==3):
	for line in file(inputfile, 'r'):
		if(line.startswith(course)):
			output.write(line)
			print line.strip()
output.close()