a=int(input())
t=a
sum=0
while(t!=0):
  r=t%10
  sum=sum+(r*r*r)
  t=t//10
if(sum==a):
  print("yes")
else:
  print("no")
