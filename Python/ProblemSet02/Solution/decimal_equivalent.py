a = input('Enter a binary number : ')
ar = [int(i) for  i in a]
ar  = ar[::-1]
res = []
for i in range(len(ar)):
	res.append(ar[i]*(2**i))
sum_res = sum(res)		
print('Decimal Number is : ',sum_res)
