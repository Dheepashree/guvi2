a=input()
x=[]
y=[]
for i in a:
  x.append(i)
l=len(x)
for j in range(0,l-1,2):
  c=x[j]
  x[j]=x[j+1]
  x[j+1]=c
  y.append(x[j])
  y.append(x[j+1])
for m in range(0,l):
  print(y[m],end="")
