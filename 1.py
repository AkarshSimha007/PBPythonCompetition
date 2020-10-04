t=int(input())
difference=list()
for test in range(t):
    mini=0
    maxi=0
    envolope_No=int(input())
    money=list()
    input_string = input()
    money=input_string.split()
    employees=int(input())
    money = list(map(int, money))
    money.sort()
    mini=int(money[0])
    maxi=int(money[employees-1])
    difference.append(maxi-mini)
for x in difference:
  print(x)
    
    
