a = [int(j) for j in input().split()]
a.sort()
# print(a)
# 4 8 0 3 4 2 0 3
a = [l for l in a if a.count(l)>1]

print(*list(set(a)))