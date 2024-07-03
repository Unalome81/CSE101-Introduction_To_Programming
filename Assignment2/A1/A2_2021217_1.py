def Specific():
    s=input("Enter the word: ")
    f=open("question1_input.txt","r")
    L=f.read().split()
    f.close()
    n=0
    for i in L:
        if i==s:
            n+=1
    print("Word Count= ",n)
    return 

def Unique():
    f=open("question1_input.txt","r")
    L=f.read().split()
    f.close()
    R=[]
    S=set()
    for i in range(len(L)):
        if L[i] not in S:
            S.add(L[i])
            R.append(L[i]+";")
    x=R[len(R)-1][:len(R[len(R)-1])-1]+"."
    R.pop()
    R.append(x)
    print(*R)
    return

def All_Count():
    f=open("question1_input.txt","r")
    L=f.read().split()
    f.close()
    Dict={}
    for i in L:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    for i in Dict:
        print(i+" : "+str(Dict[i]))
    return

def Replace():
    f=open("question1_input.txt","r")
    L=[i.strip() for i in f.readlines()]
    f.close()
    s1=input("Enter the word you want to replace: ")
    s2=input("Enter the word you want to replace it with: ")
    for i in range(0,len(L)):
        J=L[i].split()
        for k in range(0,len(J)):
            if(J[k]==s1):
                J[k]=s2
        L[i]=J[0]
        for m in range(1,len(J)):
            L[i]=L[i]+" "+J[m]
    g=open("question1_input.txt","w")
    for n in range(0,len(L)):
        g.write(L[n]+"\n")
    return

ch=0
while ch!=6:
    print("Enter your choice:\n 1. Display specific word count\n 2. Display all unique words\n 3. Display all word counts\n 4) Replace word\n 5) Quit")
    ch=int(input())
    if ch==1:
        n=Specific()
    elif ch==2:
        Unique()
    elif ch==3:
        All_Count()
    elif ch==4:
        Replace()
    elif ch==5:
        print("Program Terminated")
        break
    else:
        print("Wrong Input")        