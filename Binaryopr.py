def add(bin1, bin2):
    sum = ""
    carry = 0
    i = len(bin1) - 1
    j = len(bin2) - 1
    while i >= 0 or j >= 0 or carry == 1:
        if i >= 0:
            digit1 = int(bin1[i])
            i -= 1
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(bin2[j])
            j -= 1
        else:
            digit2 = 0
        sumdigit = digit1 + digit2 + carry
        carry = sumdigit // 2
        sum = str(sumdigit % 2) + sum
    return sum

def subtract(bin1, bin2):
    diff = ""
    borrow = 0
    i = len(bin1) - 1
    j = len(bin2) - 1
    while i >= 0 or j >= 0 or borrow == 1:
        if i >= 0:
            digit1 = int(bin1[i])
            i -= 1
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(bin2[j])
            j -= 1
        else:
            digit2 = 0
        if digit1 < digit2:
            digit1 += 2
            borrow = 1
        else:
            borrow = 0
        diffdigit = digit1 - digit2 - borrow
        diff = str(diffdigit) + diff
    return diff

def multiply(bin1, bin2):
    prod = "0"
    bin2 = bin2[::-1]
    for i in range(len(bin2)):
        if bin2[i] == '1':
            prod = add(bin, bin1 * (2 ** i))
    return prod

def division(bin1, bin2):
    quot = "0"
    rem = bin1
    while int(rem, 2) >= int(bin2, 2):
        rem = subtract(rem, bin2)
        quot =add(quot, "1")
    return quot, quot, rem

print("Enter + For Addition")
print("Enter - For Subtraction")
print("Enter * For Multiplication")
print("Enter / For Division")
opr=(input("Enter your operation"))
no1=(input("Enter first binary number"))
no2=(input("Enter second binary number"))
if opr == '+':
    print(add(no1,no2))
elif opr == '-':
    print(subtract(no1,no2))
elif opr == '*':
    print(multiply(no1,no2))
elif opr == '/':
    print(division(no1,no2))
else:
    print("Invalid Input")