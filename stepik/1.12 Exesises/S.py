import math
a = input()
if a=='tr':
	s,d,f=float(input()),float(input()),float(input())
	p=(s+d+f)/2
	print(math.sqrt(p*(p-s)*(p-d)*(p-f)))
elif a=='okr':
	s = float(input())
	pi=3.14
	print(s**2*pi)
elif a=='pr':
	s,d = float(input()),float(input())
	print(s*d)