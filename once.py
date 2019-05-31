a=int(input())
b=input().split()
l=len(b)
count=0
for i in range(0,l):
  count=0
  for j in range(i+1,l):
    if(int(b[i])==int(b[j])):
      count=count+1
  if(count==0):
    print(b[i])
    break
    
        
