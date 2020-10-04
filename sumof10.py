def getSum(n): 
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10) 
        n = int(n/10) 
    if(sum==10):
      return True
    else: return False;

t=int(input())
count=list()
for i in range(t):
    lst=list()
    x=int(input())
    y=int(input())
    for n in range(x,y):
      result=getSum(n)
      if(result==True):lst.append(n)
    count.append(len(lst))
for i in count:
  print(i)
    