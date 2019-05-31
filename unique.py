a=int(input())
b=input().split()
l=len(b)
z=[]
for i in range(0,l):
  for j in range(i+1,l):
    if b[i] not in z:
      if(int(b[i])==int(b[j])):
        z.append(b[i])
if(z==[]):
  print("unique")
else:
  for x in range(0,len(z)):
    print(z[x],end=" ")
