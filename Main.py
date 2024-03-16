log=input("Do you have an account? (y/n)")
logid,logpwd="",""
i=0
while i==0  :
    if log=='y':
        userid=input("Enter your UserID")
        pwd=input("Enter Your Password")
        if userid == logid:
            if pwd == logpwd:
                i=1
    elif log=='n':
        logid=input("Enter Your Email ID")
        logpwd=input("Enter your Password")
    else:
        print("Invalid Input!")
while i==1:
    print("1. Open Converter")
    print("2. Open Operator")
    opr=input("Enter Your choice")
    n=0
    while n==0:
        if opr==1:
            print("1. to convert Binary Number to others")
            print("2. to convert Decimal Number to others")
            print("3. to convert Hexadecimal Number to others")
            print("4. to convert Octal Number To others")
            con=input("Enter your choice!")
            if con==1:
                import Binarytoany
            elif con==2:
                import Decimaltoany
            elif con==3:
                import Hexatoany
            elif con==4:
                import Octaltoany
            else:
                print("Invalid Input!")
            n=int(input("Do you want to continue or go out? (0 for yes/1 for no)"))
        elif opr==2:
            print("1. to do arithmetic operation of Binary Numbers")
            print("2. to do arithmetic operation of Decimal Numbers")
            print("3. to do arithmetic operation of Hexadecimal Numbers")
            print("4. to to do arithmetic operation of Octal Numbers")
            op=input("Enter your Choice: ")
            if op==1:
                import Binaryopr
            elif op==2:
                import Decimalopr
            elif op==3:
                import Hexaopr
            elif op==4:
                import OctalOpr
            else:
                print("Invalid Input!")
            n=int(input("Do you want to continue or go out? (0 for yes/1 for no)"))
        else:
            print("Invalid Input!")
            n=int(input("Do you want to continue or go out? (0 for yes/1 for no)"))
            break
        print("Do You Want to LogOut")
        i=0