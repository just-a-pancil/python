a,s,d = int(input()),int(input()),int(input())
maxval= 0
minval = 0
mdval = 0
if max(a,s) == a:
	maxval = a
	minval = s
elif max(a,s) == s:
	maxval = s
	minval = a


if max(maxval, d) == d:
	mdval = maxval
	maxval = d
elif max(maxval, d) == maxval:
	if min(minval, d) == d:
		mdval = minval
		minval = d
	elif min(minval, d) == minval:
		mdval = d
print(maxval,minval,mdval,sep='\n')
# print (maxval)
# print (minval)
# print(max(a,s))