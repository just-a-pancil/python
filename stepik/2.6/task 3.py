# lst = [int(j) for j in input().split()]
# w = int(input())
# # print(type(lst[2]))
# if w in lst:
# 	for i in range(lst.count(w)):
# 		print(lst.index(w), end = ' ')
# 		lst[lst.index(w)] = w+1
# else:
# 	print('Отсутствует')
# 5 8 2 7 8 8 2 4

numbers = [int(i) for i in input().split()]
needed = int(input())
if needed not in numbers:
    print("Отсутствует")
else:
    [print(i, end=" ") for i, x in enumerate(numbers) if x == needed]