mistnosti = ["obývák", "chodba", "sklep", "trůnní sál","jídelna"]
chodby = [[1, 2,4], [0,4], [0], [1, 2],[1,0]]
zamcene_chodby = [[], [3], [], [],[]]
inventar = {"klic" : False, "moje zlato":0,"burger":False}
cena_burgeru=15
sytost=4
mistnost_s_klicem = 2
zlato = [1, 0, 10, 300,15]
hrac = 0
skore = 0
kroky = 0

def je_cislo(mozna_cislo):
    try:
        int(mozna_cislo)
        return True
    except ValueError:
        return False
def hotovo():
    return sum(zlato) == 0
while not hotovo():
    print("mas sytost",sytost)
    if inventar["burger"]:
        print("mas burger")
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    kam_lze_jit = chodby[hrac]

    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])
    if zlato[hrac] > 0:
        print("Moznost X : sebrat", zlato[hrac], "zlata")
    if hrac == mistnost_s_klicem:
        print("Moznost C : sebrat klíč")
    if inventar["klic"] and zamcene_chodby[hrac]:
        print("Moznost R : odemknout dveře ->", mistnosti[zamcene_chodby[hrac][-1]])
    if hrac == 4 or inventar["burger"]:
        print("moznost J: najíst se")
    if hrac == 4 and inventar["moje zlato"] >= cena_burgeru:
        print("prodavačka říká:Chceš burger?řekni b")

    vstup_ok=False
    while not vstup_ok:
        vstup = input("> ")
        if not inventar["klic"] and mistnost_s_klicem==hrac and vstup=="c":
            vstup_ok=True
        elif zlato[hrac] and vstup=="x":
            vstup_ok=True
        elif (hrac==4 or inventar["burger"]) and vstup=="j":
            vstup_ok=True
        elif vstup=="r" and hrac==1 and zamcene_chodby[hrac]:
            vstup_ok=True
        elif hrac == 4 and inventar["moje zlato"] >= cena_burgeru and not inventar["burger"] and vstup=="b":
            vstup_ok=True
        elif je_cislo(vstup) and int(vstup) <= len(kam_lze_jit) and int(vstup) > 0:
            vstup_ok=True

    if vstup == "x":
        skore += zlato[hrac]
        inventar["moje zlato"]+=zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "c":
        inventar["klic"] = True
        mistnost_s_klicem = -1
    elif vstup=="j":
        sytost=11
        if not hrac==4:
            inventar["burger"]=False
    elif vstup == "b":
        inventar["burger"]=True

    elif vstup == "r":
        cilova_mistnost = zamcene_chodby[hrac].pop()
        chodby[hrac].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
    else:
        hrac = kam_lze_jit[int(vstup) - 1]

    sytost-=1
    kroky += 1
    if sytost == 0:
        print("umřels hlady")
        break
if sytost > 0:
    print("Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")
