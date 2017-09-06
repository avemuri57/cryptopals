import operator

from utils import find_key


def main():
	#Assumes that the first line of the file is line 0
	f = open('4.txt','r')
	highest_sorted_results = []
	idx = 1
	for line in f:
		sorted_results = find_key(line.rstrip())
		highest_sorted_results.append((sorted_results[0][0],sorted_results[0][1],idx))
		print((line,idx))
		idx = idx +1

		

	sorted_highest_results = sorted(highest_sorted_results,key = lambda x: x[1],reverse=True)
	print(sorted_highest_results[0])

if __name__ == "__main__":
	main()