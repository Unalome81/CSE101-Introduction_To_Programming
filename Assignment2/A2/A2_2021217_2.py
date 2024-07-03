import math
def multiply(T,X,Y,Z):
    for i in range(len(X)):
        R=[X[i],Y[i],Z[i],1]
        Res=[0]*4
        for j in range(0,len(T)):
            for k in range(0,len(R)):
                Res[j]+=T[j][k]*R[k]
        X[i]=Res[0]
        Y[i]=Res[1]
        Z[i]=Res[2]
    return

def Scaling(X,Y,Z):
    sx=float(input(("Enter sx: ")))
    sy=float(input(("Enter sy: ")))
    sz=float(input(("Enter sz: ")))
    T=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    multiply(T,X,Y,Z)
    return

def Translating(X,Y,Z):
    tx=float(input(("Enter tx: ")))
    ty=float(input(("Enter ty: ")))
    tz=float(input(("Enter tz: ")))
    T=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    multiply(T,X,Y,Z)
    return

def Rotation(X,Y,Z):
    print(" 1) Enter 1 for rotation around X-axis. \n 2) Enter 2 for rotation around Y-axis. \n 3) Enter 3 for rotation around Z-axis.")
    ch2=int(input("Enter: "))
    if ch2==1 or ch2==2 or ch2==3:
        z=float(input("Enter the angle of rotation(in radians): "))
    T=[]
    if(ch2==1):
        T=[[1,0,0,0], [0,math.cos(z),-math.sin(z),0], [0,math.sin(z),math.cos(z),0], [0,0,0,1]]
    elif(ch2==2):
        T=[[math.cos(z),0,math.sin(z),0], [0,1,0,0], [-math.sin(z),0,math.cos(z),0], [0,0,0,1]]
    elif(ch2==3):
        T=[[math.cos(z),-math.sin(z),0,0], [math.sin(z),math.cos(z),0,0], [0,0,1,0], [0,0,0,1]]
    else:
        print("Wrong Input")
    if ch2==1 or ch2==2 or ch2==3:
        multiply(T,X,Y,Z) 
    return

n=input("Enter number of vertices: ")
X0=[float(i) for i in input().split()]
Y0=[float(i) for i in input().split()]
Z0=[float(i) for i in input().split()]
X=X0.copy()
Y=Y0.copy()
Z=Z0.copy()
q=int(input("Enter number of queries: "))
T=[]
for i in range(0,q):
    print(" 1) Enter 1 for scaling. \n 2) Enter 2 for translating. \n 3) Enter 3 for rotation.")
    ch1=int(input("Enter your choice: "))
    ch2=0    
    if ch1==1:
        Scaling(X,Y,Z)        
    elif ch1==2:
        Translating(X,Y,Z)       
    elif ch1==3:
        Rotation(X,Y,Z)    
    print("X= ",*X)
    print("Y= ",*Y)
    print("Z= ",*Z)
f=open("Transformations.txt","w")
f.write("Input:\n X="+" ".join([str(i) for i in X0]))
f.write("\n Y="+" ".join([str(i) for i in Y0]))
f.write("\n Z="+" ".join([str(i) for i in Z0]))
f.write("\nOutput:\n X="+" ".join([str(i) for i in X]))
f.write("\n Y="+" ".join([str(i) for i in Y]))
f.write("\n Z="+" ".join([str(i) for i in Z]))
f.close()