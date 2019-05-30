a=input().split()
x=a[0]
y=a[1]
c=0
d=0
w=[]
z=[]
for i in x:
  z.append(i)
  l1=len(z)
  for m in range(0,l1-1):
    if(z[m]==z[m+1]):
      c=c+1
for j in y:
  w.append(j)
  l2=len(w)
  for n in range(0,l2-1):
    if(w[n]==w[n+1]):
      d=d+1
if(c==d):
  print("yes")
else:
  print("no")
