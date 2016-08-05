C_INPUT = raw_input(">")
crypt = bytearray.fromhex(C_INPUT)
crypt_array = []
print "="*40
i=0
k=0
j = 1

while i < len(crypt):
	crypt_array.append(crypt[i])
	i+=1
crypt_array2 = crypt_array
print crypt_array
while j < len(crypt_array):
	count = 0 
	while k < len(crypt_array):
		crypt_array2_1 = crypt_array2[0:len(crypt_array2)-j]
		print crypt_array2_1


			
		if crypt_array[k+j] == crypt_array2_1[k]:
			count += 1
			k+=1
		print "Key", j , "count" , k
		j+=1

