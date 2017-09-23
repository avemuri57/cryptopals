from utils import break_repeated_key_xor


data = open('6.txt')
file = data.read().replace('\n', '').decode('base64')	
print break_repeated_key_xor(file)




