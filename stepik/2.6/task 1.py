s = []
a = int(input())
s.append(a)
while sum(s)!=0:
	a = int(input())
	s.append(a)
d = [j*j for j in s]
print(sum(d))