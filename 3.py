import operator

from utils import find_key

INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def main():
	results = find_key(INPUT)
	print results[0:3]
	return results



if __name__ == "__main__":
	main() 