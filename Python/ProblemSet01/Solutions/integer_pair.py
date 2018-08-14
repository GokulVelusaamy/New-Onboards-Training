ar = []
flag = 0
number = input('Enter a number')
for i in range(6):
	ar.append(number**i)
for i in ar:
	if(i == number):
		print number,"Power and Number are Equal"
		flag = 1
		break
if (flag == 0):
	print "Number and power are not equal"
#print(ar)
