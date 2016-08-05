a = 187
i = 0
while i < 256 :
	cypher = a ^ i
	print chr(cypher)
	i+=1
