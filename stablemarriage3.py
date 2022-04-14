import time
import sys

peopleamount = int(input())
men = [None]*peopleamount
women = [None]*peopleamount

# Loop over all the numbers and create men and women lists with following structure
# man: [index, first_choice, second_choice, ...]
# woman: [reference to current man/ None if single, rating_of_man1, rating_of_man2, ....]

def read_input():
	inputlist = []
	#Store all the input numbers in a list
	while len(inputlist)<2*peopleamount*(peopleamount+1):
		for x in input().split():
			inputlist.append(int(x))

	for i in range(2*peopleamount):
		index = inputlist[i*(peopleamount+1)]-1
		temp = inputlist[i*(peopleamount+1):i*(peopleamount+1)+peopleamount+1]
		if women[index] == None:
			temp2 = [None]*(peopleamount+1)
			#Swap from preference list to rating list for quicker look up
			for j, t in enumerate(temp): #O(n)
				temp2[t] = j
			women[index] = temp2
		else:
			men[index] = temp

start = time.time()
read_input()
read_input_time = time.time()-start

start = time.time()
while len(men) is not 0:
	m = men.pop(0) #Next man to propose
	w = women[m.pop(1)-1] #His first choice
	current_partner = w[0] #Her current partner, None if single
	if not current_partner: #If shes free they create a pair
		w[0] = m 
	elif w[m[0]] < w[current_partner[0]]: #If shes not free but prefers the new guy, swap and put the previous guy back in the queue
		w[0] = m
		men.append(current_partner) 
	else: #If she prefers her current partner nothing happens except the current proposing man cant propose to the same woman again
		men.append(m)
gale_shapley_time = time.time()-start

#Print the results 

for w in women:
	print(w[0][0])
print("----------------------------------")
print("Read input time:", read_input_time)
print("Gale Shapley time:", gale_shapley_time)
print("Total", read_input_time+gale_shapley_time)
print("----------------------------------")

































