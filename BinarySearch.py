def binary_search(list , item):
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
item1= 645
item2= 0
print(str(item),'index','is',binary_search(list,item))
print(str(item1),'index','is',binary_search(list,item1))
print(binary_search(list,item2))
