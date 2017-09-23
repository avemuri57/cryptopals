from __future__ import division

def base64_to_hex(b64str):
    return b64str.decode('base64').encode('hex').rstrip()


def hex_to_base64(hexstr):
    return hexstr.decode('hex').encode('base64').rstrip()

def fl_xor(x,y):
    if len(x) != len(y):
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

def repeating_key_xor(intxt, key):
    outtxt = ""

    for i, c in enumerate(intxt):
        outtxt += chr(ord(c) ^ ord(key[i % len(key)]))

    return outtxt

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

def find_key_bin(input):
    x = input
    max_score = 0
    winner = ''
    results = []
    for i in range(256):
        buffx = chr(i)*len(x)
        result = fl_xor(buffx,x)
        score = analyze_freq(result)
        results.append((result,score))

    sorted_results = sorted(results,key=lambda x:x[1],reverse=True)
    return sorted_results[0]

def generate_rep_key(key,strlen):
	reps = strlen/len(key)
	mod = strlen % len(key)
	return reps*key + key[:mod]


def hamming_distance(str1,str2):
    return sum([bin(ord(chr1)^ord(chr2)).count('1')  for chr1, chr2 in zip(str1,str2)])

def repeating_key_xor(intxt, key):
    outtxt = ""

    for i, c in enumerate(intxt):
        outtxt += chr(ord(c) ^ ord(key[i % len(key)]))

    return outtxt

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

def char_freq(chars):
    freq = 0
    most_freq_letters = 'etaoinhs'

    for c in chars:
        if c in most_freq_letters:
            freq += 1

    return freq


def break_single_byte(ctxt):
    freqs = []

    for key in range(0xFF + 1):
        chars = []
        for c in ctxt:
            chars.append(chr(ord(c) ^ key))
        freqs.append(char_freq(chars))

    return freqs.index(max(freqs))

def find_key_length(file):
    avg_hamming_dist = []
    for KEYSIZE in range(2,41):
        b1, b2, b3, b4 = file[:KEYSIZE], file[KEYSIZE:2*KEYSIZE], \
            file[2*KEYSIZE:3*KEYSIZE], file[3*KEYSIZE:4*KEYSIZE]
        dists, blocks = [], [b1, b2, b3, b4]

        for i in range(len(blocks)-1):  
            dists.append(hamming_distance(blocks[i],blocks[i+1])/KEYSIZE)

        avg_hamming_dist.append((sum(dists) / len(dists), KEYSIZE))

    print(sorted(avg_hamming_dist)[:5])
    return sorted(avg_hamming_dist)[:5]


def break_repeated_key_xor(file):
    best_freq, ptxt = 0, ''
    key_length = find_key_length(file)

    for _, KEY_SIZE in key_length:
        key = ''
        blocks =['']*KEY_SIZE
        for i,c in enumerate(file):
            blocks[i % KEY_SIZE] += c

        for block in blocks:
            key += chr(break_single_byte(block))

        txt = repeating_key_xor(file,key)
        cur_freq = char_freq(txt)

        if cur_freq > best_freq:
            best_freq = cur_freq
            ptxt = txt
            best_key_size = KEY_SIZE
            best_key = key

    return best_key

