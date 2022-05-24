import math
import sys


def dist(p1,p2):# Simple distance function
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	
def compare(p_x): #O(n^2) quadratic algorithm comparing distances between x-sorted players return distance between closest pair.
	min_dist = math.inf
	for i, point1 in enumerate(p_x):
		j = i + 1
		while j < len(p_x):
			point2 = p_x[j]
			delta = dist(point1,point2)
			if delta < min_dist:
				min_dist = delta
			j += 1
	return min_dist



#Sorting in ascending order
def sortPoints(players):
	p_x = sorted(players, key = lambda s: s[0]) #Sorting coordinates by only looking at x-coordinates
	p_y = sorted(players, key = lambda s: s[1]) #Sorting coordinates by only looking at y-coordinates
	return p_x, p_y

#Complexity O(nLogn)
def closest(p_x, p_y, n):
	if n < 4:
		return(compare(p_x))

	mid = n//2
	middle_point = p_x[mid]
	left_x = p_x[:mid]
	right_x = p_x[mid:]
	left_y = []
	right_y = []

	for p in p_y:
		if p[0] <= middle_point[0]:# If y-coordinate is less than or equal to x-coordinate of middle point, add point to left list. otherwise right list 
			left_y.append(p)
		else:
			right_y.append(p)

	# Recursive call for min dist in both halves
	min_dist_in_halves = min(closest(left_x, left_y, mid), closest(right_x, right_y, n - mid))

	s_y = [] # All points in strip sorted on y
	for p in p_y:
		if abs(middle_point[0] - p[0]) < min_dist_in_halves: #if point is within area between halves.
			s_y.append(p)

	# Is only O(n) because inner loop runs only for the few points in the strip. 
	for i in range(len(s_y)):
		j = i + 1
		while j < len(s_y) and (s_y[j][1] - s_y[i][1]) < min_dist_in_halves: #If distance between points y-coordinate is less than minimal distance
			min_dist_in_halves = min(dist(s_y[j], s_y[i]), min_dist_in_halves) # Comparing to other distances, assigning that value to min_dist resulting in closest pair.
			j += 1
	return min_dist_in_halves

# Main
N = int(input())  # reading number of people and pairs

players = []

for i in range(N):  # reading descriptions
    coordinate = (sys.stdin.readline().replace('\n','').split(' '))
    players.append(list(map(int, coordinate)))

p_x, p_y = sortPoints(players)
res = "%.6f" %round(closest(p_x,p_y,N),6) # six decimals
print(res)