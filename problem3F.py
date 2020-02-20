import numpy as np
import random
import matplotlib.pyplot as plt
import re

def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1

def romanToDecimal(str): 
    res = 0
    i = 0
    while (i < len(str)): 

        s1 = value(str[i]) 
  
        if (i+1 < len(str)): 

            s2 = value(str[i+1]) 

            if (s1 >= s2): 
                res = res + s1 
                i = i + 1
            else: 
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
  
    return res 
def main():
	file = open('5.txt', encoding="utf8")
	maxlen = 0
	textfile = file.read()
	lens = np.array([])
	wordict = {}

	#isolate each words
	words = textfile.replace('\n', ' ').replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').replace(';', ' ').split() 

	last = ""
	for word in words:
		last_lowered = last.lower()
		lowered = word.lower()
		if(last_lowered == "chapter"):

			if(word.isalpha() and not word in wordict):
				wordict[word] = 1

		last = word


	print(wordict)
	chapters = 0
	for Roman in wordict:
		chapters = max(chapters,romanToDecimal(Roman))


	print(chapters)


if __name__ == "__main__":
    main()		