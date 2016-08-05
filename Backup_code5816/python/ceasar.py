INPUT = raw_input("> ")
j = 0
INPUT = INPUT.lower()
INPUT = INPUT.replace(" ","")
fo =  open("cipher1.txt","a+")
while j < 27:
	print "\n","="*40,j
	for i in INPUT:
		num = ord(i)
		decrypt = num + j
		if decrypt > ord('z'):
			decrypt-=26
		elif decrypt< ord("a"):
			decrypt+=26
		print chr(decrypt),

	j+=1
