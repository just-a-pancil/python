a,b = int(input()),int(input())
sch1 = 1

while sch1%a>0 or sch1%b>0:
  sch1 += 1
print(sch1)