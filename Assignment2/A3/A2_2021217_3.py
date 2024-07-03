import math

def dec_r(num,r):
    n=float(num)
    res=""
    div=int(math.log(n,int(r)))
    while(div>-7):
        quo=int(n/(int(r)**div))
        res+=L[quo]
        n-=quo*(int(r)**div)
        div-=1
        if(div==-1):
            res+="."
    return res

def r_dec(n,r): 
    res=0
    pos=0
    if("." in n):
        rad=n.index(".")
        pos=len(n[0:rad])-1
    else:
        pos=len(n)-1           
    
    for i in n:
        if i==".":
            continue
        dig=L.index(i)
        res+=int(dig)*(int(r)**pos)
        pos-=1
    return str(res)

def check(n,r):
    L2=L[0:int(r)]
    chk=True
    for i in n:
        if i==".":
            continue
        if i not in L2:
            chk=False
    return chk

def choice():
    print('''Menu:
    1) Convert decimal to binary and vice-versa
    2) Convert decimal to hexadecimal and vice-versa
    3) Convert decimal to octal and vice-versa.
    4) Convert binary to hexadecimal and vice-versa.
    5) Convert binary to octal and vice-versa.
    6) Convert hexadecimal to octal and vice-versa.
    7) Convert number with radix A to radix B. Here A,B <= 36. In this case, you must take A,B as input.
    8) To Exit''')
    c=int(input("\n Enter your choice: "))
    return c

def L_Create():
    L=[]
    for i in range (10):
        L.append(str(i))
    for j in range(65,91):
        L.append(chr(j))
    return L

L=L_Create()
c=0
ch=0
while(c!=8):
    br=1
    A=0
    B=0
    c=choice()
    if c==1:
        print('''
        1) To convert decimal to binary
        2) To convert binary to decimal''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,10)
            A=10
            B=2
        else:
            chk=check(n,2)  
            A=2
            B=10  
    elif c==2:
        print('''
        1) To convert decimal to hexadecimal
        2) To convert hexadecimal to decimal''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,10)
            A=10
            B=16
        else:
            chk=check(n,16)  
            A=16
            B=10  
    elif c==3:
        print('''
        1) To convert decimal to octal
        2) To convert octal to decimal''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,10)
            A=10
            B=8
        else:
            chk=check(n,8)  
            A=8
            B=10  
    elif c==4:
        print('''
        1) To convert binary to hexadecimal
        2) To convert hexadecimal to binary''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,2)
            A=2
            B=16
        else:
            chk=check(n,16)  
            A=16
            B=2
    elif c==5:
        print('''
        1) To convert binary to octal
        2) To convert octal to binary''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,2)
            A=2
            B=8
        else:
            chk=check(n,8)  
            A=8
            B=2
    elif c==6:
        print('''
        1) To convert octal to hexadecimal
        2) To convert hexadecimal to octal''')
        ch=int(input("Enter: "))        
        if ch!=1 and ch!=2:
            br=0
        n=input("Enter the number: ")       
        if ch==1:
            chk=check(n,2)
            A=2
            B=8
        else:
            chk=check(n,8)  
            A=8
            B=2
    elif c==7:
        A=input("Enter radix A (between 2 and 36 both included): ")
        if int(A)<2 or int(A)>36:
            br=0
        else:
            n=input("Enter the number with radix A: ")
            chk=check(n,A)  
            if chk:
                B=input("Enter radix B (between 2 and 36 both included): ")
                if int(B)<2 or int(B)>36:
                    br=0
    elif c==8:
        print("Program Terminated")
        break
    else:
        print("Wrong Input")

    if br:    
        if chk:
            print("The converted number is: "+dec_r(r_dec(n,A),B))
        else:
            print("The number you entered does not match with the required radix.")
    else:
        print("Wrong Input")     

    pause=input("Enter any alphanumeric value to continue: ")