a = int(input())
s = [[g] *g for g in range(1,a+1)]
v = sum(s, [])[:a]
print(*v)