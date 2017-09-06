def base64_to_hex(b64str):
    return b64str.decode('base64').encode('hex').rstrip()


def hex_to_base64(hexstr):
    return hexstr.decode('hex').encode('base64').rstrip()



def fl_xor(x,y):
    if len(x) is not len(y):
        print('Buffers not the same length')
        return
    else:
        l = [chr(ord(a)^ord(b)) for a,b in zip(x,y)]
        return "".join(l)


def analyze_freq(str):
	lstr = list(str)
	score = 0
	for x in lstr:
		if x.lower() in scoring_chart.keys():
			score += scoring_chart[x.lower()]
	return score

#This is specifically for single character keys
def find_key(input):
	x = input.decode('hex')
	max_score = 0
	winner = ''
	results = []
	for i in range(256):
		buffx = chr(i)*len(x)
		result = fl_xor(buffx,x)
		score = analyze_freq(result)
		results.append((result,score))

	sorted_results = sorted(results,key=lambda x:x[1],reverse=True)
	return sorted_results
	

def generate_rep_key(key,strlen):
	reps = strlen/len(key)
	mod = strlen % len(key)
	return reps*key + key[:mod]

scoring_chart = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}



