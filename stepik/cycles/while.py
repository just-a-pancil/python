sch = 0
c = int(input())
if c!=0:
  sch += c
  c = int(input())
  while c!=0:
    sch+=c
    c = int(input())
print(sch)