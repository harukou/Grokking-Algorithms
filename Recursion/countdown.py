def countdown(x):
	print(x)
	if x <= 1:
		return 'end'
	else:
		return countdown(x-1)

k = countdown(5)
print(k)