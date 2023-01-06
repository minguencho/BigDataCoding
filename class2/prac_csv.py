#csv.py

#module
import csv, os, codecs

with codecs.open('./class2/b.csv','r','utf-8') as f:
    csvfile2 = f.read()
print(csvfile2)