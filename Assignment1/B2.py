def value(t,c,d,e,r):
    x=e[0]+t*d[0]
    y=e[1]+t*d[1]
    z=e[2]+t*d[2]
    disq=(x-e[0])**2+(y-e[1])**2+(z-e[2])**2-r**2
    return disq

def finput():
    L=[]
    L.append(float(input("x= ")))
    L.append(float(input("y= ")))
    L.append(float(input("z= ")))
    return L
def distance():
    return
e=[]
d=[]
c=[]
print("Enter the coordinates of the sphere's origin- ")
c=finput()
r=float((input("Enter the radius: ")))
print("The line that we will take will be of the form: P(t)=e+(d*t)")
print("Enter the coordinates of e: ")
e=finput()
print("Enter the value of vector d: ")
d=finput()
res1=-1
res2=-2
ch=0
for t in range(0,1001):
    sq=value(t,c,d,e,r)
    if(sq<=0):
        res1=t
        ch=1
    if(ch==1 and t<res1 and sq>=0):
        res2=t-1
        ch+=1
        break
if(ch==0):
    print("There are no point of intersections")
elif(ch==1):
    print("There are two points of intersections")
    print("First one is between t=",res1,"and t=", res1+1)
    print("Second one is between t=",res2,"and t=", res2+1)
elif(ch==2):
    print("There is only one point of intersections")
    print("It is between t=",res1,"and t=", res1+1)
    
    


    


