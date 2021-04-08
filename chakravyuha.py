N=int(input())
c=[]
for i in range(N):
    c.append([])
for i in range(N):
    for j in range(N):
        c[i].insert(j,0)
n=N
r=0
d=N-1
l=0
u=0
cnt=1
flag=1
k=0
s=1
p=[[0,0]]
while(n>0 and flag==1):
    for j in range(k,n):
        c[r][j]=cnt
        if(cnt%11==0):
            s=s+1
            p.append([r,j])
        cnt=cnt+1
        if (r==d):
            flag=0
    r=r+1
    k=k+1
    for i in range(r,n):
        c[i][d]=cnt
        if(cnt%11==0):
            s=s+1
            p.append([i,d])
        cnt=cnt+1
    d=d-1
    n=n-1
    for j in range(d,l,-1):
        c[n][j]=cnt
        if(cnt%11==0):
            s=s+1
            p.append([n,j])
        cnt=cnt+1
    l=l+1
    for i in range(n,l-1,-1):
        c[i][u]=cnt
        if(cnt%11==0):
            s=s+1
            p.append([i,u])
        cnt=cnt+1
    u=u+1
for i in range(N):
    for j in range(N):
        print(c[i][j],end=" ")
    print()
print("Total Power points:",s)
for i in p:
    print(tuple(i))
    

    
    
