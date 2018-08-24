a = int(input('Enter a number :'))
b = int(input('Enter another number :'))
if(a%b == 0):
	res1 = b**a
	res2 = int(b**(a/b))
print(b,' power ', a, 'is ', res1)
print(b,' power ', int(a/b), 'is ', res2)
