def modify_list(a):
	l = []
	# print(a)
	# print(m)
	[l.append(o//2) for o in a if o%2 == 0]
	a.clear()
	# print(a)
	[a.append(j) for j in l]
	# print(l)
# a = [int(j) for j in input().split()]
# modify_list(a)
# print(a) 