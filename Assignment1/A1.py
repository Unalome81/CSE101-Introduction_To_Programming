def Right_Angled (n):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
    return

def Isosceles (n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(1,(2*i)):
            print(k,end="")
        print()
    return

def Kite (n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(1,(2*i)):
            print(k,end="")
        print()
    
    for i in range(1,n):
        for j in range(1,i+1):
            print(" ",end="")
        for k in range(1,2*(n-i)):
            print(k,end="")
        print()    
    return

def Half_Kite (n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
    for i in range(1,n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()
    return

def X(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end="")
        for k in range(1,2*(n-i+1)):
            print(k,end="")   
        print()
    for i in range(2,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(1,(2*i)):
            print(k,end="")
        print()
    return

print("Welcome to pattern Generator: \n\n")

exit = 0

while(exit != "1"):
    print ("You have the following choices: \n")
    print("\n 1 Right-angled triangle \n 2) Isosceles triangle \n 3) Kite \n 4) Half Kite \n 5) X \n")

    choice=input("Enter your choice:")

    if (choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="5"):
        n=int(input("Enter the number of rows:"))
        if (choice=="1"):
            Right_Angled(n)
        elif (choice=="2"):
            Isosceles(n)
        elif (choice=="3"):
            Kite(n)
        elif (choice=="4"):
            Half_Kite(n)
        elif (choice=="5"):
            X(n)
        else:
            print("Wrong Input")

        exit = input("Press 1 to exit and any other character to continue: ")

print("Exit Successful!")
