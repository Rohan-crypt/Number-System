def add(hex1, hex2):
    dec1 = int(hex1, 16)
    dec2 = int(hex2, 16)
    sum = dec1 + dec2
    sum = hex(sum).split('x')[-1].upper()
    return sum

def sub(hex1, hex2):
    dec1 = int(hex1, 16)
    dec2 = int(hex2, 16)
    diff = dec1 - dec2
    diff = hex(diff).split('x')[-1].upper()
    return diff
num1=input("Enter an hexadecimal number")
num2=input("Enter an hexadecimal number")
print("Enter + if you want addition")
print("Enter - if you want subtraction")
opr=(input())
if opr == '+':
    print(add(num1,num2))
elif opr == '-':
    print(sub(num1,num2))
else:
    print("Invalid input")