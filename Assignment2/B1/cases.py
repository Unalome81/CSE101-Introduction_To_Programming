import math
def function1(x):
    return math.pow(x,5)

def generateData():
    n=int(input("Enter the number of inputs you want to give: "))
    for i in range(n):
        f=open("IP"+str(i+1),"w")
        f.write(input("Enter: "))
        f.close()

    for j in range(n):
        f=open("IP"+str(j+1),"r")
        g=open("OP"+str(j+1),"w")
        ip=int(f.read())
        op=int(function1(ip))
        g.write(str(op))
        f.close()
        g.close()
    return n

