def create(name):
    f=open(name,"r")
    D={}
    L=[i.strip() for i in f.readlines()]
    for i in L:
        sp=i.index(" ")
        D[i[0:sp]]=i[sp+1:len(i)]
    return D

Akey=create("Q4\\Admin\\AnswerKey.txt")
RStud=create("Q4\\Admin\\RegisteredStudents.txt")
Omr={}
Marks={}
for i in RStud:
    Omr[i]=create("Q4\\Student\\"+i+"_"+RStud[i]+".txt")
for i in RStud:
    sum=0
    for j in Akey:
        if Omr[i][j]==Akey[j]:
            sum+=4
        elif Omr[i][j]=="-":
            pass
        else:
            sum-=1
    Marks[i]=sum
f=open("FinalReport.txt","w")
for i in RStud:
    f.write(str(i)+" "+RStud[i]+" "+str(Marks[i])+"\n")