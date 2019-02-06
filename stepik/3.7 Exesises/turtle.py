n = int(input())
x,y = 0,0
commands = ['север', 'запад','юг',"восток"]
for i in range(n):
	inp = input()
		com = inp.split()[0]
		step = int(inp.split()[1])
	if com == commands[0]:
		x -= step
	elif com == commands[2]:
		x += step
	elif com == commands[1]:
		y += step
	elif com == commands[3]:
		y -= step
print(x,y)