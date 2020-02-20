import numpy as np
import random
import matplotlib.pyplot as plt
import re
file1 = open('1.txt', encoding="utf8")
file2 = open('2.txt', encoding="utf8")
file3 = open('3.txt', encoding="utf8")
file4 = open('4.txt', encoding="utf8")
file5 = open('5.txt', encoding="utf8")
file6 = open('6.txt', encoding="utf8")
files = [file1,file2,file4,file6]
wordict = {}

for file in files:
	textfile = file.read()
	lens = np.array([])	
	words = textfile.replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').replace(';', ' ').split() 

	for word in words:	
		if(word.isalpha() and word.islower()):
			
			lens = np.append(lens,[len(word)])
			if(word in wordict.keys()):
				wordict[word] +=1
			else:
				wordict[word] = 1
	print(len(lens))


newfile1 = open('6.txt', encoding="utf8")
testfile1 = newfile1.read()
arr  = np.array([])
f= open("output6.txt","w+")
words1 = testfile1.replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').replace(';', ' ').split() 
for word in words1:
	if(word.isalpha() and word.islower()):
		if(wordict[word] == 1):
			f.write(" ")
			f.write(word)
			arr = np.append(arr,word)
print("unuque:", len(arr))

