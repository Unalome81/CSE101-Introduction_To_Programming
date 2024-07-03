def Normal(L,n):
    J=[]
    for i in range(n):
        for j in range(n):
            J.append(L[i][j])
    print("Normal Traversal: "+" ".join(J))
    return

def Alternate(L,n):
    J=[]
    for i in range(n):
        if i%2==0:   
            a=0
            b=len(L) 
            c=1
        else:
            a=len(L)-1
            b=-1
            c=-1
        for j in range(a,b,c):
            J.append(L[i][j])  
    print("Alternate Traversal: "+" ".join(J)) 
    return

def Spiral(L,n):
    t=0
    l=0
    r=n-1
    b=n-1
    J=[]
    while(l<=r):
        for i1 in range(l,r+1):
            J.append(L[t][i1])
        t+=1
        if l==r:
            break
        for i2 in range(t,b+1):
            J.append(L[i2][r])
        r-=1
        for i3 in range(r,l-1,-1):
            J.append(L[b][i3])
        b-=1
        if l==r:
            break
        for i4 in range(b,t-1,-1):
            J.append(L[i4][l])
        l+=1
    print("Spiral traverse: "+" ".join(J))

def Boundary(L,n):
    J=[]
    for i1 in range(n):
        J.append(L[0][i1])
    for i2 in range(1,n):
        J.append(L[i2][n-1])
    for i3 in range(n-2,-1,-1):
        J.append(L[n-1][i3])
    for i4 in range(n-2,0,-1):
        J.append(L[i4][0])
    print("Boundary Traversal: "+" ".join(J)) 
    return

def RLD(L,n):
    J=[]
    for i in range(2*n-1):
        if(i<n):
            r=0
            c=i
        else:
            r=i-n+1
            c=n-1
        while(r<n and c>=0):
            J.append(L[r][c])
            r+=1
            c-=1
    print("Right to left diagonal traversal: "+" ".join(J))
    return

def LRD(L,n):
    J=[]
    for i in range(2*n-1):
        if(i<n):
            r=0
            c=n-1-i
        else:
            r=i-n+1
            c=0
        while(r<n and c<n):
            J.append(L[r][c])
            r+=1
            c+=1
    print("Left to Right diagonal traversal: "+" ".join(J)) 
    return

n=int(input("Enter the value of n in the nXn matrix: "))
L=[]
for i in range(n):
    L.append([j for j in input().split()])
    ch=0
while(ch!=7):
    print('''Enter: 
    1) Normal traversal( from left to right for each row)
    2) Alternating traversal ( first left to right for the first row, then right to left for the second row,
    then left to right for the third row, and so on.)
    3) Spiral traversal from outer to inwards
    4) Boundary traversal.(First, traverse the upper boundary from left to right, then right
    boundary from up to down, then bottom boundary from right to left and at last from left
    boundary from down to up)
    5) Diagonal traversal from right to left
    6) Diagonal traversal from left to right.
    7) Exit''')
    ch=int(input())
    if ch==1:
        Normal(L,n)
    elif ch==2:
        Alternate(L,n)
    elif ch==3:
        Spiral(L,n)
    elif ch==4:
        Boundary(L,n)
    elif ch==5:
        RLD(L,n)
    elif ch==6:
        LRD(L,n)
    elif ch==7:
        print("Program Terminated")
    else:
        print("Wrong Input")
    if(ch>0 and ch<7):
        k=input("Enter any alphanumeric value to continue: ")
