class Student:
    def __init__(self, n, cg, br):
        self.name=n
        self.cgpa=cg
        self.branch=br
        self.isPlaced=False

    def isEligible(self, comp):
        return (self.cgpa>comp.requiredcgpa)*(self.branch in comp.branches)*(not self.isPlaced)
    
    def apply(self, comp):
        comp.appliedStudents.append(self)
    
    def getPlaced(self):
        self.isPlaced=True

class Company:
    def __init__(self, n, req, br, open):
        self.name=n
        self.requiredcgpa=req
        self.branches=br
        self.positionOpen=open
        self.appliedStudents=[]
        self.applicationOpen=True

    def hireStudents(self):
        R=self.appliedStudents.copy()
        n=len(self.appliedStudents)
        for i in range(n):
            for j in range(n-1):
                if R[j].cgpa<R[j+1].cgpa:
                    t=R[j]
                    R[j]=R[j+1]
                    R[j+1]=t
        if len(R)>self.positionOpen:
            for i in range (len(R)-self.positionOpen):
                R.pop()

        print("\nThe company "+self.name+" has hired the following students: ")
        for k in R:
            k.getPlaced()
            print(k.name)
        self.closeApplication()

    def closeApplication(self):
        self.applicationOpen=False
        if len(self.appliedStudents)<self.positionOpen:
            x=len(self.appliedStudents)
            self.positionOpen-=len(self.appliedStudents)
        else:
            x=self.positionOpen
            self.positionOpen=0
        print("\nThe company has hired ", x, " students")

n=int(input("Enter the number of students: "))
St=[]
for i in range(n):
    print("\nEnter the name of student ", (i+1))
    nam=input()
    cg=-1
    while(cg<0 or cg>10):
        print("Enter the cgpa of student ", (i+1))
        cg=float(input())
        try:
            assert not (cg<0 or cg>10), "Invalid CGPA"
        except AssertionError as message:
            print(message)
    print("Enter the branch of student ", (i+1))
    br=input()
    St.append(Student(nam, cg, br))

print()
q=int(input("Enter the number of companies: "))
Com=[]
for i in range(q):
    print("\nEnter the name of company ", (i+1))
    nam=input()
    cg=-1
    while(cg<0 or cg>10):
        print("Enter the required cgpa of company ", (i+1))
        cg=float(input())
        try:
            assert not (cg<0 or cg>10), "Invalid CGPA"
        except AssertionError as message:
            print(message)
    print("Enter the eligible branches for company ", (i+1))
    BR=[j for j in input().split()]
    print("Enter the number of positions open for this company:")
    pos=int(input())
    Com=Company(nam, cg, BR, pos)
    print()
    for j in St:
        if j.isEligible(Com):
            j.apply(Com)
            print("Student ", j.name, " is eligible for the company ", Com.name)
        else:
            print("Student ", j.name, " is not eligible for the company ", Com.name)
    Com.hireStudents()