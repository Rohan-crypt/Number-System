def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

n1=int(input("Enter Frist Number"))
n2=int(input("Enter Second Number"))
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
opr=input("Enter the operation you want to perform:")
if opr == '+':
    print(add(n1,n2))
elif opr == '-':
    print(subtract(n1,n2))
elif opr=='*':
    print(multiply(n1,n2))
elif opr =='/':
    print(division(n1,n2))
else:
    print("Invelid Input!")