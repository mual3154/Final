import random

n = input("Enter the number of spears & humans present: ") #asks the user for the amount n for the amount of spears and people 
ppl = [ ] #Creates a new empty list of people
spears = [ ] #Creates a new empty list of spears
x = 0 #ensuring the list traverse starts from 0
for x in range(n): #traverses the list and gives the 
	ppl.append(random.randint(1,100)) #random integer (shortest person, tallest person) -> (1,100) any different values can be put here!
	spears.append(random.randint(1, 100)) #random integer for the upper and lower bounds of the size of spears

ppl.sort() #sorts the humans for ease
#the code below will sort the spears list

order = 0 #starts the order of sortedspears from 0
sortedspears = [ ] #new list to pop from spears into this list based on height difference
for travppl in range(n): #traverses the list of people assuming that both ppl and spears are size n
	minindex = 0 #index containing the found minimum with a person & spear
	minvalue =  abs(ppl[travppl] - spears[minindex]) # initial minvalue is with the first in spears[]
	for travspears in range(len(spears)): #traverses the spears list 
		diff = abs(ppl[travppl] - spears[travspears]) #the loop checking every element in spears and then giving the outer for loop the index with the smallest difference
		if(minvalue > diff): #checks the difference with the recorded minvalue
			minvalue = diff #if is is the smallest then the minvalue will be updated
			minindex = travspears #minindex is updated 
	popped = spears.pop(minindex) #the minimum difference is popped into popped
	sortedspears.insert(order, popped) #popped is then put into sorted spears 
	order = order + 1 #this moves the sortedspears forward one to have all the ppl in line with their spears
	
y = 0 #initial value of for loop to traverse through the sortedspears and ppl
for y in range(n):
	diff = abs(ppl[y] - sortedspears[y])
	print ("The person with the height of {0} is holding a spear with the height {1} with a height difference of {2}".format(ppl[y], sortedspears[y], diff))
	