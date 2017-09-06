from utils import fl_xor

INPUT = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
KEY = "ICE"
RESULT = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def main():
	reps = len(INPUT)/len(KEY)
	mod = len(INPUT) % len(KEY)

	rep_key = reps*KEY + KEY[:mod]
	result = fl_xor(rep_key, INPUT)
	print(result.encode('hex') == RESULT)

if __name__ == "__main__":
	main()