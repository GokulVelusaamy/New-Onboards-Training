a, b, c = input("Enter numbers: ")
ar = [a,b,c]
odd_array = [i for i in ar if(i%2!=0)]
if len(odd_array)>=1:
	odd_max = max(odd_array)
	print(odd_max)
else:
	print('There are no Odd Numbers')
