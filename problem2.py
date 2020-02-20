# find all possible combinations of 0 and 1 with a sequence size of 5. Example: 10011, 11001
import numpy as np
import random
import matplotlib.pyplot as plt
numdict  = {}
count = 0
for i in range(1000):
	num = (random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))
	if(not num in numdict.values()):
		numdict[count] = num
		count +=1 
for i in range(len(numdict)):
	print(numdict[i])


