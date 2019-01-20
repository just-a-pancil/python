a,b = int(input()),int(input())
c,d = int(input()),int(input())
print('\t', end = '')
for j in range(c,d+1):
	print(j, end = '\t')
print()
for i in range(a,b+1):
	print(i, end = '\t')
	for g in range(c,d+1):
		print(i*g, end = '\t')
	print()