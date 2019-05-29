a=input().split()
x=int(a[0])
y=int(a[1])
for z in range(x+1,y):
  i=2
  count=0
  if(z==2):
    print(z,end=" ")
  else:
    while(i<z):
      if(z%i==0):
        count=count+1
        break
      else:
        i=i+1
        continue
      if(count==1):
        continue
      else:
        print(z,end=" ")
  
  
