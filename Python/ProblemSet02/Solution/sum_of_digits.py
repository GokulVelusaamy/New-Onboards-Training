class Error(Exception):
	pass
class ValueisZeroError(Error):
   pass
def sumDigits(s):
	try:
		ar = [int(i) for i in a if i.isdigit()]
		#print(ar)
		res = sum(ar)
		if res == 0:
			raise ValueisZeroError
		print('Addition of Decimal digits is :', res)
	except ValueisZeroError:
		print('Given String has no numbers')
	
	
a = input('Enter a string with numbers : ')
sumDigits(a)
