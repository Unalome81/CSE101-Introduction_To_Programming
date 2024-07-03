def buy(s,g,n,L):
    for i in range(m):
        if(L[i][g]=='1'):
            L[i][g]=s
    return

def transform(p,q,m,n,L):
    H=[]
    pr=0
    qr=0
    for i in range(n):
        z=0
        for j in range(m):
            if(L[j][i]=='1'):
                z+=1
        H.append(z)
    flip=0
    str=""
    S=set()
    for i in range(n):
        gr=-1
        for j in range(n):
            if(j not in S):
                if(gr==-1):
                    gr=j
                elif H[gr]<H[j]:
                    gr=j
        S.add(gr)
        if flip%2==0:
            str="D"
            pr+=p*H[gr]
        else:
            str="S"
            qr+=q*H[gr]
        buy(str,gr,n,L)
        flip+=1
        p+=1
        q+=1
    return pr,qr,L

print("Enter the number of grammy's won by Doja Dog and DJ Snack: ")
p,q=[int(i) for i in input().split()]
print("Enter the height and the number of skyscrapers in the city: ")
m,n=[int(i) for i in input().split()]
L=[]
print("Enter the initial layout of Fanville: ")
for i in range(m):
    L.append([j for j in input().split()])
pr,qr,L=transform(p,q,m,n,L)
print("Final reputation of Doja Dog and DJ Snack: ")
print(pr,qr)
print("Final Layout of fanville: ")
for i in range(m):
    print(*L[i])