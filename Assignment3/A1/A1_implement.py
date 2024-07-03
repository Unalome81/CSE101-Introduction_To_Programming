import math
def matmul(T,B):
    Res=[]
    for i in range(len(T)):
        sum=0
        for j in range(len(B)):
            sum+=T[i][j]*B[j]
        Res.append(sum)   
    return Res

def scale(x, y, z, sx, sy, sz):
    T=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    B=[x,y,z,1]
    return matmul(T, B)

def translate(x, y, z, tx, ty, tz):    
    T=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    B=[x,y,z,1]
    return matmul(T, B)

def rotate(x, y, z, axis, phi):  
    phi*=3.14159/180  
    if(axis=='X'):
        T=[[1,0,0,0], [0,math.cos(phi),-math.sin(phi),0], [0,math.sin(phi),math.cos(phi),0], [0,0,0,1]]
    elif(axis=='Y'):
        T=[[math.cos(phi),0,math.sin(phi),0], [0,1,0,0], [-math.sin(phi),0,math.cos(phi),0], [0,0,0,1]]
    elif(axis=='Z'):
        T=[[math.cos(phi),-math.sin(phi),0,0], [math.sin(phi),math.cos(phi),0,0], [0,0,1,0], [0,0,0,1]]
    B=[x,y,z,1]
    return matmul(T,B) 

# n=int(input("Enter number of vertices: "))
# X=[float(i) for i in input().split()]
# Y=[float(i) for i in input().split()]
# Z=[float(i) for i in input().split()]
# X0=X.copy()
# Y0=Y.copy()
# Z0=Z.copy()
# q=int(input("Enter number of queries: "))
# for i in range(0,q):
#     print(" 1) Enter 1 for scaling. \n 2) Enter 2 for translation. \n 3) Enter 3 for rotation. \n 4) Enter 4 to exit")
#     ch=int(input("Enter your choice: "))   
#     if ch==1:
#         sx=float(input(("Enter sx: ")))
#         sy=float(input(("Enter sy: ")))
#         sz=float(input(("Enter sz: ")))
#         for i in range(n):
#             X[i], Y[i], Z[i], bin=scale(X[i], Y[i], Z[i], sx, sy, sz)   
       
#     elif ch==2:
#         tx=float(input(("Enter tx: ")))
#         ty=float(input(("Enter ty: ")))
#         tz=float(input(("Enter tz: ")))
#         for i in range(n):
#             X[i], Y[i], Z[i], bin=translate(X[i], Y[i], Z[i], tx, ty, tz)     
              
#     elif ch==3:
#         print(" 1) Enter 'X' for rotation around X-axis. \n 2) Enter 'Y' for rotation around Y-axis. \n 3) Enter 'Z' for rotation around Z-axis.")
#         axis=input()         
#         phi=float(input("Enter the angle of rotation(in degrees): "))
#         for i in range(n):
#             X[i], Y[i], Z[i], bin=rotate(X[i] ,Y[i] ,Z[i] , axis, phi) 
#     elif ch==4:
#         print("Program Terminated")     
#         break 
#     print("Transformed vertices:")
#     print("X= "+" ".join([str(i) for i in X]))
#     print("Y= "+" ".join([str(i) for i in Y]))
#     print("Z= "+" ".join([str(i) for i in Z]))
# f=open("Transformations.txt","w")
# f.write("Input:\n X="+" ".join([str(i) for i in X0]))
# f.write("\n Y="+" ".join([str(i) for i in Y0]))
# f.write("\n Z="+" ".join([str(i) for i in Z0]))
# f.write("\nOutput:\n X="+" ".join([str(i) for i in X]))
# f.write("\n Y="+" ".join([str(i) for i in Y]))
# f.write("\n Z="+" ".join([str(i) for i in Z]))
# f.close()