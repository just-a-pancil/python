z = int(input())
s,d,f = 'programmistov','programmist','programmista'
a= z % 100
if a <= 20:
	if a == 1:
		print(z,d)

	if 2 <= a <= 4:
		print(z,f)

	elif 5 <= a <= 20 or a == 0:
		print(z,s)

else:
	a = a % 10
	if a == 1:
		print(z,d)
	if 2 <= a <= 4:
		print(z,f)

	elif 5 <= a <= 20 or a == 0:
		print(z,s)

