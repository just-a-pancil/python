objects = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l = []
se = set(objects)
for i in objects:
	if i not in se:
		l.append(i)
print(len(l))