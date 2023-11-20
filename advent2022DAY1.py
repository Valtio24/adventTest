
total = []
current = []
vtotal=[]
with open("nbrDeCalories.txt") as f:
    for l in f.readlines():
        current.append(l.replace("\n",""))
        if l == "\n":
            total.append(current)
            current=[]
total.append([l,""])        
print(total)

tot=0
for i in range(len(total)):
    for j in range(len(total[i])-1):
        tot+=int(total[i][j])
    vtotal.append(tot)
    tot=0
print(vtotal)





for i in range(len(vtotal)): 
    for j in range(i+1, len(vtotal)): 
        if vtotal[i] > vtotal[j]: 
            vtotal[i],vtotal[j]=vtotal[j],vtotal[i]

print(vtotal)
print(vtotal[-1],vtotal[-2],vtotal[-3])
print(vtotal[-1]+vtotal[-2]+vtotal[-3])









    
    

        
        



