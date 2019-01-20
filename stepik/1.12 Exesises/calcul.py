a,s=float(input()),float(input())
d=input()
# print(type(d))

# print (d)
if (d=="/" or d=='div' or d=='mod') and s==0:
	print("Деление на 0!")
else:
	if d == '+':
		print(a+s)
	elif d=='-':
		print(a-s)
	elif d=='/':
		print(a/s)
	elif d=='*':
		print(a*s)
	elif d=='mod':
		print(a%s)
	elif d=='pow':
		print(a**s)
	elif d=='div':
		print(a//s)