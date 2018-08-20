def getRatios(vect1, vect2):
	vect_res = []
	try:
		for i in range(len(vect1)):
			vect_res.append(vect1[i]/vect2[i])
		print ("Result Array",vect_res)

	except ZeroDivisionError:
		print("Divide by Zero Error")


vect1 = []
vect2 = []
print("Enter 5 values for array 1 and array 2 each")		
print("Array 1")
for i in range(5):
	a = int(input())
	vect1.append(a)
print("Array 2")	
for i in range(5):
	b= int(input())
	vect2.append(b)

getRatios(vect1,vect2)	
