import cases
def function2(x):
    y=1
    for i in range(5):
        y*=x
    return y
def testing(n):
    check=1
    for i in range(n):
        f=open("IP"+str(i+1),"r")
        g=open("OP"+str(i+1),"r")
        ip=int(f.readline())
        op1=int(g.readline())
        op2=function2(ip)
        if op1!=op2:
            check=0
        f.close()
        g.close()
    if check==1:
        print("SUCCESS")
    else:
        print("FAILED")
    return

n=cases.generateData()
testing(n)