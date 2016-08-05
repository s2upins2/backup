import string as str
fo = open("cipher1.txt", "a+")
letter = "abcdefghijklmnopqrstuvwxy"
cipher = raw_input("> ")
i =0
while  i < len(cipher):
	no = int(cipher[i]) + (int(cipher[i+1])-1)*5
	fo.write(letter[no-1])
	i+=2