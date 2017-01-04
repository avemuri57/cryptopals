#Fixed XOR

b1='1c0111001f010100061a024b53535009181c'
b2='686974207468652062756c6c277320657965'
solution= '746865206b696420646f6e277420706c6179'


def fixed_hex_xor(s1,s2):
	s1=s1.decode('hex')
	s2=s2.decode('hex')
	return ("".join(chr(ord(x)^ord(y)) for x,y in zip(s1,s2))).encode('hex')



if fixed_hex_xor(b1,b2) == solution:
	print "Successfully Solved this Challenge"
else:
	print "Fail"