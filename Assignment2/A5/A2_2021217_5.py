def noteCreate():
    L=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    Maj=[2,2,1,2,2,2,1]
    Min=[2,1,2,2,1,2,2]
    f=open("scalemajor.txt","w")
    g=open("scaleminor.txt","w")
    for i in range(len(L)):
        s=""
        p1=i
        p2=i
        s1=[]
        s2=[]
        s1.append(L[p1])
        s2.append(L[p2])
        for j in range(len(Maj)):
            p1+=Maj[j]
            if L[p1%12] in s1:
               s1.append(L[p1%12])
               s1[len(s1)-1]+="'"
            else:
                s1.append(L[p1%12])
           
            p2+=Min[j]           
            if L[p2%12] in s2:
               s2.append(L[p2%12])
               s2[len(s2)-1]+="'"
            else:
                s2.append(L[p2%12])
        
        f.write(' '.join(s1)+"\n")
        g.write(' '.join(s2)+"\n")
    f.close()
    g.close()

def majorNotes(root):
    f=open("scalemajor.txt","r")
    L=[i.strip() for i in f.readlines()]
    f.close()
    for i in L:
        J=i.split()
        if J[0]==root:
            return J
    return
    

def minorNotes(root):
    f=open("scaleminor.txt","r")
    L=[i.strip() for i in f.readlines()]
    f.close()
    for i in L:
        J=i.split()
        if J[0]==root:
            return J
    return

noteCreate()
root=input("Enter the root note: ")
ch=input("Enter the type of scale (Major/Minor): ")
if ch=="Major":
    print("Major scale in the key of "+root+" is: ")
    print(*majorNotes(root))
elif ch=="Minor":
    print("Minor scale in the key of "+root+" is: ")
    print(*minorNotes(root))
else:
    print("Wrong Input")

