a=input()
count=0
for i in a:
  if(i=='I'):
    count=count+1
  elif(i=='V'):
    if(count>=1 and count<5):
      count=5-count
    else:
      count=count+5
  elif(i=='X'):
    if(count==1):
      count=10-count
    else:
      count=count+10
print(count)
      
