s = raw_input('Enter Decimal number string').split(',')
sum = 0
#if len(s)>=1:
for i in s:
	sum = sum+float(i)
print "Sum of Decimal Numbers is :",sum	
