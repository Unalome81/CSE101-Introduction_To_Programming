class LaundryServices:
    def __init__(self, nam, cont, em, ty, br, sea):
        global ID
        ID+=1
        self.id=ID
        self.name=nam
        self.contact=cont
        self.email=em
        self.type=ty
        self.brand=br
        self.season=sea
    
    def customerDetails(self):
        print("\nCustomer ID- ", self.id)
        print("Name- ", self.name)
        print("Contact No.- ", self.contact)
        print("Email- ", self.email)
        print("Type- ", self.type)
        if self.brand==True:
            print("Branded")
        else:
            print("Not Branded")
    
    def calculateCharge(self):
        if self.type=="Cotton":
            price=50
        elif self.type=="Silk":
            price=30
        elif self.type=="Woolen":
            price=90
        elif self.type=="Polyester":
            price=20          
        if self.brand==True:
            br=1.5
        else:
            br=1
        if self.season=="Winter":
            sea=0.5
        else:
            sea=1
        price*=br*sea
        return price

    def finaldetails(self):
        self.customerDetails()
        tot=self.calculateCharge()
        print("Total Charge= ", tot)
        if tot>200:
            print("To be returned in 4 days")
        else:
            print("To be returned in 7 days")

ID=0
Laundry=[]
q=int(input("Enter the number of customers: "))
for i in range(q):
    nam=input("\nName of the customer: ")
    cont=int(input("Contact Number: "))
    em=input("Email: ")
    ty=input("Type of cloth- ")
    br=bool(input("Branded?(Enter 0 for No and 1 for Yes): "))
    sea=input("Season: ")
    Laundry.append(LaundryServices(nam, cont, em, ty, br, sea))
print("\nCustomer specific details: ")
for i in Laundry:
    i.finaldetails()      