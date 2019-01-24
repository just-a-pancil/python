# yey :D
def mid(*q):

    local_string = q[0].split(';')
    del local_string[0]


    w = []
    [w.append(int(j)) for j in local_string]


    if len(q)>1:
        # print(int(local_string[q[1]]))
        q[2].append(int(local_string[q[1]]))
    else:
        # print(str(sum(w)/3))
        return round(sum(w)/3, 19)
# print(mid([1,2,3]))



stringToPrint = []
exam0,exam1,exam2=[],[],[]

with open('dataset_3363_4.txt', encoding="utf8") as file:
    for string in file:
        string.strip()

        stringToPrint.append(mid(string))

        # print(stringToPrint)
        mid(string,0,exam0)
        mid(string,1,exam1)
        mid(string,2,exam2)
    # print(sum(exam0)/3,sum(exam1)/3,sum(exam2)/3,sep = ' ')




with open('qwqw.txt', 'w') as file:
    for i in stringToPrint:
        file.write(str(i)+'\n')
    file.write(str(round(sum(exam0)/3,11))+' ')
    file.write(str(round(sum(exam1)/3,11))+' ')
    file.write(str(round(sum(exam2)/3,91))+' ')