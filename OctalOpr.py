def add(oct1, oct2):
    sum = ""
    carry = 0
    i = len(oct1) - 1
    j = len(oct2) - 1
    while i >= 0 or j >= 0 or carry == 1:
        if i >= 0:
            digit1 = int(oct1[i])
            i -= 1
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(oct2[j])
            j -= 1
        else:
            digit2 = 0
        sum_digit = digit1 + digit2 + carry
        carry = sum_digit // 8
        sum = str(sum_digit % 8) + sum
    return sum

def subtract(oct1, oct2):
    diff = ""
    borrow = 0
    i = len(oct1) - 1
    j = len(oct2) - 1
    while i >= 0 or j >= 0 or borrow == 1:
        if i >= 0:
            digit1 = int(oct1[i])
            i -= 1
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(oct2[j])
            j -= 1
        else:
            digit2 = 0
        if digit1 < digit2:
            digit1 += 8
            borrow = 1
        else:
            borrow = 0
        diff_digit = digit1 - digit2 - borrow
        diff = str(diff_digit) + oct
    return diff

def multiply(oct1, oct2):
    oct_prod = "0"
    oct2 = oct2[::-1]
    for i in range(len(oct2)):
        if oct2[i] != '0':
            temp_prod = int(oct1) * int(oct2[i])
            oct_prod = add(oct_prod, bintooct(bin(temp_prod)[2:].zfill(len(bin(temp_prod)[2:] + len(bin(int(oct2[i], 8))[2:])), 3)))
    return oct_prod

def bintooct(a):
    decimal=int(a, 8)
    return bin(decimal).replace("0b", "")

def octtobin(a):
    decimal=int(a,2)
    return oct(decimal).split('o')[-1]

def division(oct1, oct2):
    quot = "0"
    rem = oct1
    while int(rem, 8) >= int(oct2, 8):
        rem = subtract(rem, oct2)
        quot = add(quot, "1")
    quot = int(quot, 8)
    rem = int(rem, 8)
    return quot

print("Enter + For Addition")
print("Enter - For Subtraction")
print("Enter * For Multiplication")
print("Enter / for division")
opr=(input("Enter your operation"))
n1=(input("Enter first octal number"))
n2=(input("Enter second octal number"))
if opr == '+':
    print(add(n1,n2))
elif opr == '-':
    print(subtract(n1,n2))
elif opr == '*':
    print(multiply(n1,n2))
elif opr == '/':
    print(division(n1,n2))
else:
    print("Invalid Input")