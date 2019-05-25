a=int(input())
i=2
count=0
while(i<a):
  if(a==2):
    break
  elif(a%i==0):
    count=count+1
    break
  else:
    i=i+1
    continue
if(count==1):
  print("no")
else:
  print("yes")
  
  
