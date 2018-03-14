def quickSort(arr):
	if len(arr)<2:
		return arr
	else:
		pivot = arr[0]
		less = [x for x in arr[1:] if x<=pivot]
		greater = [x for x in arr[1:] if x>pivot]
		return quickSort(less) + [pivot] +quickSort(greater)

arr = [23,234,5,523,352,2,4523,4]
sorted = quickSort(arr)
print(sorted)		