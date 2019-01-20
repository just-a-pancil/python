st = input().lower().split()
a = set(st)
dic={}
for j in a:
	dic.update({j: st.count(j)})
[print(k,s) for k,s in dic.items()]

# my favorite:

# s=input().lower().split()
# for i in set(s):
#     print(i,s.count(i))