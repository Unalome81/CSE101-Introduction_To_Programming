i=0
print("Fn = (b1 and not b1)")
while(i<2):
    b1=bool(i)
    Fn = (b1 and not b1)
    if(Fn):
        print("Satisfiable")
        print("b1=",b1)
        break
    i+=1
if(not Fn):
    print("Unsatisfiable")
print()
print("Fn = (b1 or b2) and (b2 or not b3)")
i=0
while(i<2):
    b1=bool(i)
    j=0
    while(j<2):
        b2=bool(j)
        k=0
        while(k<2):
            b3=bool(k)
            Fn = (b1 or b2) and (b2 or not b3)
            if(Fn):
                print("Satisfiable")
                print("b1=",b1,", b2= ",b2,", b3= ",b3)
                break
            k+=1
        if(Fn):
            break
        j+=1
    if(Fn):
        break
    i+=1
        
