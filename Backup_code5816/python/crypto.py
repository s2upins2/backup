cypher = "A8EDBD"
Hex = bytearray.fromhex(cypher)
i  = 0 
while i < 256 :
	j = 0
	print "Key ",i
	while j < len(Hex):
		XOR = Hex[j] ^ i
		print chr(XOR),
		j+=1
	print "\n"
	i+=1
2 3 7 