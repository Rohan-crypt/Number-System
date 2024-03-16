num = input("Enter a binary number: ")
decimal = int(num, 2)
hexa = hex(decimal).split('x')[-1].upper()
octal= oct(decimal).split('o')[-1]