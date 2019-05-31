a=int(input())
b=input().split()
x=[]
l=len(b)
for i in range(0,l):
  x.append(b[i])
  x.sort()
for j in range(l-1,-1,-1):
  print(x[j],end="")
