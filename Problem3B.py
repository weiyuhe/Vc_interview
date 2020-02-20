import numpy as np
import random
import matplotlib.pyplot as plt
import re


file = open('1.txt', encoding="utf8")
textfile = file.read()
lens = np.array([])
#words = re.split(', |_|-|!|.', textfile)
#words = textfile.replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').split() 
words = textfile.replace('.', '.').replace('!', '.').replace('?', '.').split('.') 
print(words)
for word in words:
	if(len(word)>6):
		lens = np.append(lens,[len(word)])
	# if(word.isalpha()):
	# 	lens = np.append(lens,[len(word)])


print(max(lens))
maxlength = int(max(lens))
mybin = np.linspace(0,maxlength, maxlength+1);
plt.hist(lens, bins = mybin) 
plt.title("Pride and Prejudice") 
plt.xlabel("Length of sentence")
plt.show()