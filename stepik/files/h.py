d=''
s= ''
f=''
with open('dataset_3363_2.txt') as file:
    a = file.readline().strip()
    for i in a:
        if i.isalpha() and s =='':
            s=i
        elif i.isdigit():
            d+=i
        elif i.isalpha() and s!='':
            f += s*int(d)
            s=i
            d=''
    f += s*int(d)
        # print(s)
with open('dataset_3363_2.txt','w') as file:
    file.write(f)


# a3b4c2e10b1