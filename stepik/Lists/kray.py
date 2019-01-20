a = [int(j) for j in input().split()]
# print(a)
# 1 3 5 6 10
s = []
if len(a)==1:
	s+=a
else:
    for j in range(len(a)-1):
        s.append(a[j-1] + a[j+1])
    s.append(a[len(a)-2]+a[0])
for j in range(len(a)):
	print(s[j], end = ' ')
# print(s)