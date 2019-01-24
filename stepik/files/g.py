with open('qq.txt') as file:
    line = ''
    [line + o.strip().lower().split() for o in file]
    
    print(line)
# with open('dataset_3363_2.txt','w') as file:
#     file.write(f)


# a3b4c2e10b1