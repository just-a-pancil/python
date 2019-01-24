s=[]
with open('dataset_3363_3.txt') as file:
    for i in file:
        s+=i.lower().split()
    dic = {s.count(f) : f for f in s}
    # if max(list(dic))
    # for key in sorted(list(dic)):
    #     print(dic[key],)
    print(dic[max(list(dic))],max(list(dic)))
with open('dataset_3363_3.txt','w') as file:
    a = str(dic[max(list(dic))]) + ' ' + str(max(list(dic)))
    file.write(a)