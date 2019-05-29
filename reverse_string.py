a=input()
b=[]
for i in a:
  b.append(i)
l=len(b)
for y in range(l-1,-1,-1):
  print(b[y],end="")
