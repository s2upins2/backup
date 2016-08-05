def cut():
	C_INPUT = raw_input("> ")
	fo = open("decrypt.txt","a+")
	cypher = list(C_INPUT)
	i = 0
	while i < len(cypher):
		fo.write(cypher[i])
		i+=1
		if i % 14 == 0:
			fo.write("\n")
	fo.close()
def read():
	fo = open("decrypt.txt","r+")
	rl = fo.readline(1)
	#byte = bytearray.fromhex(rl.strip("\n"))
	print rl
def line():
	
	n = 0 
	while n < 255:
		fo = open("decrypt.txt","r+")
		for i,line in enumerate(fo) :
			byte = bytearray.fromhex(line.strip())
			cypher =  byte[0]  ^ n
			print chr(cypher),
		print "\n"
		fo.close()
		n+=1 
line()

