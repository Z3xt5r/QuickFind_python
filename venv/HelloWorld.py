id= []
sz=[]
i=0
N=0

def Create():
    print("Enter size : ")
    N= input()
    N=int(N)
    print(N)
    while i<N:
        id.append(i)
        sz.append(1)

class QuickFind:
    def Hello(self):
        print("Class Created ")
    def connected(p,q):
        return id[p]==id[q]
    def Union(p,q):
        pid= id[p]
        qid=id[q]
        for i in range(N):
            if(id[i]==pid):
                id[i]=qid

Create()
Q = QuickFind()
Q.Hello()

while true:
    print("1. Union \n 2. Connected \n 3. Exit")
    x=input()
    if(x==3):
        break
    elif (x==2):
        print("Enter Elements : ")
        p=input()
        q=input()
        if(Q.connected(p,q)):
            print("Connected")
        else:
            print("Not Connected")
    else:
        print("Enter Elements : ")
        p = input()
        q = input()
        Q.Union(p,q)



