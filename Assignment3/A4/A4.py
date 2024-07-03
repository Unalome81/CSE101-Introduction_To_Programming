class Person:
    def __init__(self, fname, lname, a):
        self.firstname=fname
        self.lastname=lname
        self.age=a

    def object_info(self):
        print(self.firstname, self.lastname, self.age)

def order1(L):
    R=L.copy()
    for i in range(len(R)):
        for j in range(len(R)-1):
            if R[j].firstname>R[j+1].firstname:
                t=R[j]
                R[j]=R[j+1]
                R[j+1]=t
    for i in R:
        i.object_info()

def order2(L):
    R=L.copy()
    for i in range(len(R)):
        for j in range(len(R)-1):
            if R[j].lastname>R[j+1].lastname:
                t=R[j]
                R[j]=R[j+1]
                R[j+1]=t
    for i in R:
        i.object_info()

def order3(L):
    R=L.copy()
    for i in range(len(R)):
        for j in range(len(R)-1):
            if R[j].age>R[j+1].age:
                t=R[j]
                R[j]=R[j+1]
                R[j+1]=t
    for i in R:
        i.object_info()
    
print("Welcome to the Application! ")
n=int(input("Specify the number of people to be enrolled: "))
L=[]
for i in range(n):
    print("For person ",i+1,": ")
    fname, lname, age=[j for j in input("Enter(firstname, lastname, age): ").split()]
    L.append(Person(fname, lname, int(age)))
q=int(input("Specify number of queries:"))
for i in range(q):
    print("\nEnter Query(firstname, lastname or age) ", i+1, ": ")
    ch=input()
    if ch=="firstname":
        order1(L)
    elif ch=="lastname":
        order2(L)
    elif ch=="age":
        order3(L)