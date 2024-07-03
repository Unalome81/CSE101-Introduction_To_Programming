def getReverse(n):
    rev=0
    while(n>0):
        rev=(rev*10)+n%10
        n=n//10
    return rev

def checkPalindrome(n):
    pal=0
    temp=n
    while(temp>0):
        pal=(pal*10)+temp%10
        temp=temp//10
    if(n==pal):
        return True
    else:
        return False

def checkNarcisstic(n):
    temp=n
    len=0
    while(temp>0):
        len+=1
        temp=temp//10
    sum=0
    temp=n
    while(temp>0):
        sum+=(temp%10)**len
        temp=temp//10 
    if(sum==n):        
        return True
    else:
        return False

def findDigitSum(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    return sum

def findSquareDigitSum(n):
    sum=0
    while(n>0):
        sum+=(n%10)**2
        n=n//10
    return sum

ch=0
while(ch!=6):
    print("Hello User, Welcome to the Application. Please select one of the following operations.")
    print("1. Find reverse of a number")
    print("2. Check whether a number is a palindrome or not.")
    print("3. Check whether a number is a Narcissistic number or not.")
    print("4. Find the sum of digits of a number.")
    print("5. Find the sum of squares of digits of a number.")
    print("6. Select 6 to exit the application.")
    ch=int(input("Enter your choice: "))
    if(ch!=6):
        n=int(input("Enter your number(non-negative): "))  
        if(n>=0):    
            if(ch==1):
                print(getReverse(n))
            elif(ch==2):
                if(checkPalindrome(n)):
                    print("It is a Palindrome Number")
                else:
                    print("It is not a Palindrome Number")
            elif(ch==3):
                if(checkNarcisstic(n)):
                    print("It is a Narcisstic Number")
                else:
                    print("It is not a Narcisstic Number")
            elif(ch==4):
                print(findDigitSum(n))
            elif(ch==5):
                print(findSquareDigitSum(n))
            else:
                print("Invalid Input")
        else:
            print("Error: Negative number has been entered.") 
    else:
        print("Program Terminated. Thank You.")
    
    
        
        