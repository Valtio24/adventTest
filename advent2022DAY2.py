toto=""
totol=""
with open("RockPapersCisors.txt") as f:
    for l in f.readlines():
        totol+=l[0]
        toto+=l[2]
total=0

for i in range (len(toto)):
    if toto[i]== "X":
        total += 1
        if totol[i]=="A" :
            total+=3
        elif totol[i]=="B" :
            total+=6
        elif totol[i]=="C" :
            total+=0
    elif toto[i]=="Y":
        total+=2
        if totol[i]=="A" :
            total+=0
        elif totol[i]=="B" :
            total+=3
        elif totol[i]=="C" :
            total+=6
    elif toto[i]=="Z":
        total+=3
        if totol[i]=="A" :
            total+=6
        elif totol[i]=="B" :
            total+=0
        elif totol[i]=="C" :
            total+=3
    # elif totol[i]=="A" and toto[i]=="X":
    #     total+=3
    # elif totol[i]=="A" and toto[i]=="Y":
    #     total+=6
    # elif totol[i]=="A" and toto[i]=="Z":
    #     total+=0
    # elif totol[i]=="B" and toto[i]=="X":
    #     total+=0
    # elif totol[i]=="B" and toto[i]=="Y":
    #     total+=3
    # elif totol[i]=="B" and toto[i]=="Z":
    #     total+=6
    # elif totol[i]=="C" and toto[i]=="X":
    #     total+=6
    # elif totol[i]=="C" and toto[i]=="Y":
    #     total+=0
    # elif totol[i]=="C" and toto[i]=="Z":
    #     total+=3

print(total)



