import random

class Person: #i created a class for this problem
	def __init__(self, rank):
		self.hit = False #includes whether or not someone is hit
		self.xpos = random.randint(-40,40) #generates a random number for the x position
		self.ypos = random.randint(-40,40) #generates a random number for the y position
		self.rank = rank #this rank is the id of the person
		self.tohit = [ ] # 

	def ydistance(self, other): #retrieves the distance in the y-coordinate system
		oy = other.ypos #takes in the y coordinate of the person
		sy = self.ypos #takes in the y coordinate from self
		return abs(sy - oy) # returns an abs value of the distance

	def xdistance(self, other): #retrieves the distance in the x-coordinate system
		ox = other.xpos #takes in the x coordinate of the person
		sx = self.xpos #takes in the x coordinate from self
		return abs(sx - ox) #returns an abs value of the distance


	def closestneighbor(self, xlist, ylist): #function for the unique nearest neighbor
		rank = self.rank #retrieves rank in order to retrieve the distances between himself and the other nodes
		currentxpath = xlist[rank] #retrieve from list of paths
		currentypath = ylist[rank] #retrieve from list of paths
		currentindex = rank #index that is returned to show who is going to be hit with a balloon
		minval = 1000 # set the minval as a high number that is never going to be exceeded
		currentdist = 0 # same as above, stores the current distance
		for l in range(len(currentypath)): #traverses through the length of the x and y list
			if (l != rank): # does not calculate the minimum if the array is at the same node
				currentdist = ((currentypath[l])**2 + (currentxpath[l])**2)**(0.5) #sqrt((x-coordinate)^2 + (y-coordinate)^2)
			if(currentdist < minval): # checks if the current minimum is greater than the calculated distance
				minval = currentdist
				currentindex = l #sets the index to be the minimum distance
		return currentindex #returns the rank of the person that is closest








n = input("Enter an odd amount of people: ") #allows for the entry of any amount but prefers odd
ppl = [ ] #array of Person objects
for q in range(n): #traverses through ppl in order to add them to the list 
	ppl.append(Person(q)) #with rank = q
	print "Created a person with the rank: " , q , "and the coordinates: (", ppl[q].xpos, " , " , ppl[q].ypos, ")"

xdistances = [[0] * n for y in range(len(ppl))] #sets 0's for the n amount of 2d array
ydistances = [[0] * n for y in range(len(ppl))]
for y in range(len(ppl)):
	for x in range(len(ppl)): #sets 2d array
		if( x == y):
			xdistances[x][y] = 0
			ydistances[x][y] = 0
		else:
			xdistances[x][y] = ppl[x].xdistance(ppl[y])
			ydistances[x][y] = ppl[x].ydistance(ppl[y])
			ydistances[y][x] = ppl[y].xdistance(ppl[x]) 
			xdistances[y][x] = ppl[y].ydistance(ppl[x])

for d in ppl:
	d.tohit = d.closestneighbor(xdistances, ydistances) #finds and retrieves the person to be hit by eacch person in ppl[]


for x in ppl: #records the hits in the objects
	tobehit = x.tohit
	ppl[tobehit].hit = True
	print x.rank , " -> " , ppl[tobehit].rank, " HIT HAS BEEN RECORDED."

for y in ppl:
	if(y.hit == False):
		print y.rank , " WAS NOT HIT BY A BALLOON"