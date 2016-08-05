INPUT = raw_input("> ")
KEY = raw_input("> ")
j = 0
INPUT = INPUT.lower()
INPUT = INPUT.replace(" ","")
fo =  open("cipher1.txt","a+")
while j < 27:
	print "\n","="*40,j
	for k in KEY:
		for i in INPUT:
			num = ord(i)
			key =  ord(k)
			decrypt = num + key
			if decrypt > ord('z'):
				decrypt-=26
			elif decrypt< ord("a"):
				decrypt+=26
			print chr(decrypt),

		
