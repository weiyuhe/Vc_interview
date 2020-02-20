
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np
import random
import matplotlib.pyplot as plt

#find all nearby node
def find_nearby(valid_dict,visited_dict,j,x,y,dt,v):
	index = j[2]
	flag = False
	count = 0
	surr = [(j[0]-1,j[1]+1), (j[0],j[1]+1), (j[0]+1,j[1]+1), (j[0]-1,j[1]),(j[0]+1,j[1]),(j[0]-1,j[1]-1),(j[0],j[1]-1),(j[0]+1,j[1]-1)]
	theta = random.uniform(0, 6.28)
	for i in range(len(surr)):
		if((not surr[i] in visited_dict.values()) and (surr[i] in valid_dict.values()) ):
			if(surr[i] == (j[0]-1,j[1]+1)):
				theta = 135*3.14/180 + random.uniform(-0.08, 0.08) #add some noise so the robot will not bounce back and forth in two angles
			elif(surr[i] == (j[0],j[1]+1)):
				theta = 90*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0]+1,j[1]+1)):
				theta = 45*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0]-1,j[1])):
				theta = 180*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0]+1,j[1])):
				theta = 0*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0]-1,j[1]-1)):
				theta = 225*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0],j[1]-1)):
				theta = 270*3.14/180 + random.uniform(-0.08, 0.08)
			elif(surr[i] == (j[0]+1,j[1]-1)):
				theta = 315*3.14/180 + random.uniform(-0.08, 0.08)
			else:
				theta = np.arccos((surr[i][0] - x)/(dt*v))
				print("ERROR in theta")

			print("theta",theta)
		else:
			print("no possible theta")
				
	return theta

def main():
	landList = [];
	listindex = 0;
	for i in range(9):
		for j in range(9):
			if (not (i>3 and j>3)):
				templist = list(landList)
				templist.append((i+1,j+1,listindex,0))
				tuple(templist)
				landList = templist
				listindex += 1

	valid_dict = {}
	for i in range(len(landList)):
		valid_dict[i] = landList[i][0:2]

	visited_land = np.asarray(landList) 

	visited_dict = {}
	vcount = 0;
	inc = 0;

	v = 0.1 # velocity is 0.1m/s
	endtime = 300; #300 second
	num = 30001;
	time = np.linspace(0,endtime, num);
	dt = endtime/(num-1);
	prevt = 0;

	theta = 0.14;
	x = 2;
	y = 3;
	location = np.array([[x,y]]);

	for t in time:
		x = x + v*np.cos(theta)*dt
		y = y + v*np.sin(theta)*dt
		new_location = np.array([[x,y]]);
		location = np.concatenate((location, new_location))

		coordinate = np.array([x, y])
		j = min(landList, key=lambda c: (c[0]- coordinate[0])**2 + (c[1]-coordinate[1])**2) #finding the cloest node

		if( not j[0:2] in visited_dict.values()):
			vcount = vcount + 1
			visited_dict[inc] = j[0:2]
			inc += 1
			tempindex = j[2]
			visited_land[tempindex][3] = 1

		if (x<0 or y<0 or x>9.5 or y>9.5 or (x>4.5 and y>4.5)):
			theta = find_nearby(valid_dict,visited_dict,j,x,y,dt,v)

		if(inc/len(landList)*100 > 75):
			print("time is: ", t)
			break #Break out of the loop when 75% of the room is cleaned
	plt.plot(location[:, 0] + 0.25, location[:, 1] + 0.25)
	plt.show()

if __name__ == "__main__":
    main()

	

