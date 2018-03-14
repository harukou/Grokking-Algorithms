#baidu baike
def gcd_recursion(x,y):
	return x if y == 0 else gcd_recursion(y,x%y)

def gcd(x,y):
	while y:
		x,y = y,x%y
	return x

x = int(input('x='))
y = int(input('y='))

print(gcd_recursion(x,y))
print(gcd(x,y))

	
