# n = int(input())
dic={}
for n in range(int(input())):
    vv=int(input())
    if vv in dic:
        print(dic[vv])
    else:
        dic.update({vv : f(vv)})
        print(dic[vv])