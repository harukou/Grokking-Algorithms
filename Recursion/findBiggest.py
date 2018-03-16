# The following is the author's answer：
def max(arr):
	if len(arr) == 2:
		return arr[0] if arr[0]>arr[1] else arr[1]
	sub_max = max(arr[1:])
	return arr[0] if arr[0]>sub_max else sub_max

arr = [342,5,46,554,745,6]

print('recursion max:',max(arr))

def max1(arr):
	max = arr[0]
	for x in range(1,len(arr)-1):
		if max<arr[x]:
			max = arr[x]
	return max

arr = [342,5,46,554,745,6]

print('loop max:',max1(arr))
