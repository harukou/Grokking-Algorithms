def count(arr):
	if arr == []:
		return 0
	return 1+count(arr[1:])

arr = [x for x in range(10)]
print(arr)
print('arr length:',count(arr))