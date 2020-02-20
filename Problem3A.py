import numpy as np
import random
import matplotlib.pyplot as plt
import re
file = open('6.txt', encoding="utf8")
textfile = file.read()
lens = np.array([])
wordict = {}
words = textfile.replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').split() 
print(words)
for word in words:
	#print(word)
	if(word.isalpha()):
		lens = np.append(lens,[len(word)])

print(lens)
plt.hist(lens, bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]) 
plt.title("Treasure Island") 
plt.xlabel("Length of words")
plt.show()

