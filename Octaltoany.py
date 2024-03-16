num=(input("Enter an octal number"))
decimal=int(num, 8)
bin= bin(decimal).replace("0b", "")
hexa= hex(decimal).replace("0x", "")