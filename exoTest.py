#tous les nombres premier inferieur a un nombre donnée


def nbrPremier(nbr):
    toto=[]
    if nbr<3:
        return ("il n'éxiste pas de nombre prmier inferrieur a 3 !")
    #un nombre premier est un nombre qui est divisible que par lui meme et 1.
    for i in range(3,nbr):
        for j in range (2,i):
            flag=True
            if i % j == 0:
                flag=False
                break
        if flag == True:
            toto.append(i)
    return toto

print(nbrPremier(23))


            


