import csv
import sys

f = open('./tasks.csv', 'r')
try:
	reader = csv.reader(f)
	for row in reader:
		if(row[0] == 'Book_ID'):
			print row[0]
		elif(row[0] == 'sy'):
			print row[0]
finally:
	f.close()