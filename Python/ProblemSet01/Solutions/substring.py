def isIn(string1,string2):
	if(string1 in string2 or string2 in string1):
		return True
	else:
		return False

string1 = raw_input('Enter string 1')
string2 = raw_input('Enter string 2')
res = isIn(string1,string2)
if res:
	print("Either of the string is a part of another string")
else:
	print("Either of the string is not a part of another string")
