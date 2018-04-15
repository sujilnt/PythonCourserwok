import csv
import sys

f = open('./input.txt', 'r')
try:
    reader = csv.reader(f)
    for row in reader:
        if(row[0] == 'a'):
            print row[1],row[2]
        elif(row[0] == 'sy'):
            print row
finally:
    f.close()