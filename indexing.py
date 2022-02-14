import csv

c = 0
row = 0
with open("/Users/jacob/Downloads/metadata.tsv") as infile:
	rd = csv.reader(infile, delimiter="\t", quotechar='"')
	for line in rd:
		if row == 0:
			print(line)
		row +=1
		if c > 4:
			break
		if 'fight' in line[2]:
			c+=1
			print('ROW:' + str(row) + line[2]+ '\n')