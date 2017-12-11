import random

def conInv(array):
	tmp = [0 for i in range(len(array))]
	return mergeSort(array, tmp, 0, len(array) - 1)

def mergeSort(array, tmp, l, r):
	count = 0
	if l < r:
		m = int((r+l)/2)

		count += mergeSort(array, tmp, l, m)
		count += mergeSort(array, tmp, m+1, r)

		count += merge(array, tmp, l, m, r)
	return count

def merge(array, tmp, l, m, r):
	k = l
	i = l
	j = m + 1
	count = 0
	while(i <= m and j <= r):
		if array[i] > array[j]:
			tmp[k] = array[j]
			count += ((m+1) - i)
			k += 1
			j += 1
		else:
			tmp[k] = array[i]
			k += 1
			i += 1

	while  i<= m:
		tmp[k] = array[i]
		k += 1
		i += 1

	while j <=r:
		tmp[k] = array[j]
		k +=1
		j +=1

	for index in range(l, r+1):
		array[index] = tmp[index]

	return count


lim = 100
array = [ ]
for x in range(lim):
	array.append(random.randint(1, 150))
print(conInv(array))