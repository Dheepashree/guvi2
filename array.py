N=int(input())
K=int(input())
a=[]
i=1
c=0
for i in range(N):
  b=int(input())
  a.append(b)
i=0
for i in range(K):
  c=c+a[i]
print(c)
