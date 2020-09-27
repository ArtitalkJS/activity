import random
NameList = []
IdToName = {1:'萝卜嘞',2:'故事里的老神仙',3:'Colsrch',4:'柒 ',5:'Xw',6:'silentcow'}
Value = {'1':'81','2':'36','3':'157','4':'14 ','5':'16','6':'7'}
f = open("happy.txt", "w",encoding='utf-8')    
for i in range(1,7):
    ValueForI = int(Value[str(i)])
    for j in range(1,ValueForI+1):
        NameList.append(i)
random.shuffle(NameList)
NameListlen = len(NameList)
HappyPerson = random.randint(0,NameListlen)
HappyPersonTwo = random.randint(0,NameListlen)
while NameList[HappyPerson] == NameList[HappyPersonTwo]:
    HappyPersonTwo = random.randint(0,NameListlen)
HappyName = IdToName[NameList[HappyPerson]]
HappyNameTwo = IdToName[NameList[HappyPersonTwo]]
f.write("Total :\t"+str(NameListlen)+"\nFirst one:\t"+str(HappyPerson)+" "+str(NameList[HappyPerson])+" "+HappyName+"\nSecond one:\t"+str(HappyPersonTwo)+" "+str(NameList[HappyPersonTwo])+" "+HappyNameTwo)
f.close()
