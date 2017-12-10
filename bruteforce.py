import random

n = input("Enter the number of spears & humans present: ") #asks the user for the amount n for the amount of spears and people 
ppl = [ ] #Creates a new empty list of people
spears = [ ] #Creates a new empty list of spears
x = 0 #ensuring the list traverse starts from 0
for x in range(n): #traverses the list and gives the 
	ppl.append(random.randint(1,100))
	spears.append(random.randint(1, 100))

for y in range(n):
	
	notmatched = True
	while(notmatched):
