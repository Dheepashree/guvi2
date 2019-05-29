a=int(input())
fact=1
if(a==0):
  fact=1
else:
  for i in range(a,0,-1):
    fact=fact*i
print(fact)
