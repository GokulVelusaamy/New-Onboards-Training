a = int(input('Enter a number1 : '))
b = int(input('Enter a number2 : '))
r = b
ar = []
while(a>r and r>0):
	r = int(a%r)
	if(r!=0):
		res = r
	#ar.append(r)
print(res)
