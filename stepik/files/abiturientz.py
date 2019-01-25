# yey :D

stringToPrint = ''
exMarks = [[],[],[]]
with open('dataset_3363_4.txt', encoding="utf8") as file:
    for string in file:
        listedStr = string.strip().split(';')
        myCount = 0
        for j in range(1,4):
            myCount += int(listedStr[j])
            exMarks[j-1].append(int(listedStr[j]))
        stringToPrint += str(myCount/3) + '\n'
        # print(stringToPrint)




with open('qwqw.txt', 'w') as qwqw:
    qwqw.write(stringToPrint)
    for i in exMarks:
        stringToPrint = str(sum(i)/len(i)) + ' '
        qwqw.write(stringToPrint)