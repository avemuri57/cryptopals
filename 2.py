from utils import fl_xor


i1 = "1c0111001f010100061a024b53535009181c"
i2 = "686974207468652062756c6c277320657965"
result ="746865206b696420646f6e277420706c6179"



def main():
    x = fl_xor(i1.decode('hex'),i2.decode('hex'))
    print(x)
    print(x.encode('hex') == result)

if __name__ == "__main__":
    main()
