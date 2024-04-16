import random
import time
random.seed(0)
seznam_cisel = []
maximum = 100
pocet = 100

for i in range(pocet):
    seznam_cisel.append(random.randint(0, maximum))

print(seznam_cisel)

def setrid(seznam):

    prohozeno = True
    while prohozeno:
        prohozeno = False

        for i in range(len(seznam) - 1):
            a = seznam[i]
            b = seznam[i + 1 ]
            if a > b:
                seznam[i] = b
                seznam[i + 1] = a
                prohozeno = True

def setridlepe (seznam):
    if len(seznam) == 1:
        return seznam
    prvni_pulka = setridlepe(seznam[:len(seznam)//2])
    druha_pulka = setridlepe(seznam[len(seznam)//2:])

    i,j =0,0
    setrideny_seznam = []

    while i < len(prvni_pulka) or j < len(druha_pulka) :
        if i == len(prvni_pulka):
            setrideny_seznam.extend(druha_pulka[j:])
            break

        if j == len(druha_pulka):
            setrideny_seznam.extend(prvni_pulka[i:])
            break

        a = prvni_pulka[i]
        b = druha_pulka[j]

        if a < b:
            setrideny_seznam.append(a)
            i += 1
        else:
            j += 1
            setrideny_seznam.append(b)

    return(setrideny_seznam)






start = time.time()
seznam = setridlepe(seznam_cisel)
konec = time.time()


print(seznam)
print("trvalo to",konec - start,"sekund")
