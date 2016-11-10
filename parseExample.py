import arff

for row in arff.load('china.arff.txt'):
	print(row.Effort);