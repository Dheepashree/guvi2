a=input()
x=a.split()
s=int(x[0])
e=int(x[1])
for i in range(s,e+1):
  if(i%2!=0):
    if(i==s):
      continue
    else:
      print(i,end=" ")
  else:
    continue
    
