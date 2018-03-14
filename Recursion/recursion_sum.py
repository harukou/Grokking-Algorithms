def recursion_sum(arr):
	if len(arr) == 1:
		return arr[0]
	elif len(arr) == 0:
		return 0
	else:
		last = arr.pop()
		return last + recursion_sum(arr)

arr = [1,3,2,4,1,1]
arr1 = [3,]
arr2 = []

print('sum arr:',recursion_sum(arr))
print('sum arr1:',recursion_sum(arr1))
print('sum arr2:',recursion_sum(arr2))
