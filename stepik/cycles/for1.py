a,b = int(input()),int(input())
s = 0
while a%3 != 0:
	a+=1
for j in range(a,b+1,3):
	s+=j
print(s/len(range(a,b+1,3)))
