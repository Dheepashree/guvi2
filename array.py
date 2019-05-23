y=input()
e=input()
x=y.split()
N=int(x[0])
K=int(x[1])
p=e.split()
i=1
c=0
for i in range(K):
  c=c+p[i]
print(c)
