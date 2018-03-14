def binary_search(list , item)
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess < item:
			low = mid + 1
		else:
			high = mid - 1
	return None
	
list = [1,3,4,6,7,123,645,3532]
item = 123
item1= 222
print(binary_search(list,item))
print(binary_search(list,item1))
