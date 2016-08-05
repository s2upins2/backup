def Check():
	if XOR < 32 : 
		False
	elif XOR < 65:
		if XOR != 44 or XOR != 45 or XOR != 46 or XOR != 32 or XOR != 58 or XOR != 59 : False
	elif XOR >91 and XOR < 97 :
		False
	elif XOR > 123 :
		False
	else : 
		True
C_INPUT = raw_input("> ")
crypt = bytearray.fromhex(C_INPUT)
n = 0
while n < 256:
	print "KEY" ,n
 	i = 0
	while i < len(crypt):
		
		XOR = crypt[i] ^ n
		print chr(XOR) ,
		i +=1
	print "\n"
	n+=1