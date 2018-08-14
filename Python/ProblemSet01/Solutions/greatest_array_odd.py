ar = []
odd_array = []
for i in range(10):
	a = input()
	ar.append(a)
	
odd_array = [i for i in ar if i%2!=0]
if(len(odd_array)>=1):
	odd_max = max(odd_array)
	print "Maximuum Odd Number is:",odd_max
else:
	print('You doesnt entered an odd number')
