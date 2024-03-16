num=(input("Enter an hexadecimal number"))
decimal = int(num, 16)
bin = bin(decimal).replace("0b", "")
octal = oct(decimal).replace("0o", "")