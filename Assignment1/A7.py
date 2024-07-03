def value(L,x):
    v=0
    for i in range(0,len(L)):
        v+=x**L[i]
    return v

def calculate_area(L,a,b,d):
    f=0
    while(a<b):
        f+=( ((a+d)-a)/6 )*( value(L,a) + 4*value(L,(a+(a+d))/2) + value(L,a+d) )
        a+=d
    return f

print("Start entering the exponent values one by one and enter \"STOP\"") 
inp=""
L=[]
while(inp!="STOP"):
    inp=input("Enter: ")
    if inp!="STOP" :
        L.append(float(inp))
a=float(input("Enter a: "))
b=float(input("Enter b: "))
d=float(input("Enter d such that b-a is divisible by d: "))
mod=b-a
while(mod>=d or (mod-d<10**(-6) and mod>0)):
    mod-=d
if mod==0 or mod<10**(-6):
    print("Area= ",calculate_area(L,a,b,d)," square units")
else:
    print("Wrong input: b-a is not divisible by d")
    

