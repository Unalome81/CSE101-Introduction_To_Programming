import datetime
class BankAccount:
    def __init__(self, user, pas, bal):
        self.username=user
        self.password=pas
        self.balance=bal
        f=open(self.username, "w")
        f.close()
    def authenticate(self):
        pas=input("Enter your secret password: ")
        if pas==self.password:
            return True
        else:
            return False
    
    def deposit(self, amt):
        n=0
        check=False
        while(not check):
            n+=1
            check=self.authenticate()
            if check==True:
                print("Authentication Successful")
                self.balance+=amt
                f=open(self.username, "a")
                f.write("\n"+str(datetime.datetime.now()) + "The amount of Rupees " + str(amt) + (" has been added. Current Balance= "+str(self.balance)))
                f.close()
            else:
                print("Wrong Password\n")
                try:
                    assert n<3, "Too many wrong attemps!!" 
                except AssertionError as msg:
                        print(msg)
                        break
    
    def withdraw(self, amt):
        n=0
        check=False
        while(not check):
            n+=1
            check=self.authenticate()
            if check==True:
                print("Authentication Successful")
                if self.balance>=amt:
                    self.balance-=amt
                    f=open(self.username, "a")
                    f.write("\n"+str(datetime.datetime.now()) + "The amount of Rupees " + str(amt) + (" has been debited. Current Balance= "+str(self.balance)))
                    f.close()
                else:
                    print("Low balance!! Cannot be debited at this time!")
            else:
                print("Wrong Password\n")
                try:
                    assert n<3, "Too many wrong attemps!!" 
                except AssertionError as msg:
                        print(msg)
                        break
    
    def bankStatement(self):    
        n=0
        check=False
        while(not check):
            n+=1
            check=self.authenticate()
            if check==True:
                print("Authentication Successful")
                f=open(self.username, "r")
                s=f.read()
                f.close()
                print("Hey ", self.username, "! Here is your bank statement:")
                print(s)
            else:
                print("Wrong Password\n")
                try:
                    assert n<3, "Too many wrong attemps!!" 
                except AssertionError as msg:
                        print(msg)
                        break

print("Welcome to the bank of IIIT Delhi\n")
user=input("Enter name: ")
pas=input("Enter password: ")
bal=int(input("Enter the starting balance: "))
Acc=BankAccount(user, pas, bal)
p=1
while(p==1):
    ch=int(input("\nSelect your option: \n1) Deposit \n2) Withdraw \n3) Bank Statement \n\nEnter:"))
    if ch==1:
        amt=int(input("Enter the amount to be deposited: "))
        Acc.deposit(amt)
    elif ch==2:
        amt=int(input("Enter the amount to be withdrawn: "))
        Acc.withdraw(amt)
    elif ch==3:
        Acc.bankStatement()
    if input("Enter Yes to continue and No to exit: ")=="Yes":
        pass
    else:
        p=0