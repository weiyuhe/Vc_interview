import numpy as np
import random
import matplotlib.pyplot as plt
import re

def check_pan(word):
	if(word.isalpha()):
		lowered = word.lower()
		a_pointer = 0
		b_pointer = len(word)-1
		while(a_pointer <= b_pointer):
			if(lowered[a_pointer] != lowered[b_pointer]):
				return False
			a_pointer += 1
			b_pointer -= 1
		return lowered
		
def main():
	file = open('6.txt', encoding="utf8")
	maxlen = 0

	textfile = file.read()
	lens = np.array([])
	wordict = {}
	words = textfile.replace('\n', ' ').replace('_', ' ').replace(', ', ' ').replace('.', ' ').replace('!', ' ').replace('"', ' ').replace('?', ' ').replace(';', ' ').split() 
	# print(words)

	for word in words:
		if(check_pan(word)):
			maxlen = max(maxlen, len(word))
			if(len(word)>2):
				print(word)
	print(maxlen)
				

if __name__ == "__main__":
    main()		

