
mistnosti = ["obývák", "chodba", "sklep", "trůnní sál"]
chodby = [[1, 2], [0], [0], [1, 2]]
zamcene_chodby = [[], [3], [], []]
klic = 2

zlato = [1, 0, 10, 300]

hrac = 0
skore = 0
kroky = 0
ma_klic = False

def je_cislo(mozna_cislo):
    try:
        int(mozna_cislo)
        return True
    except ValueError:
        return False
def hotovo():
    return sum(zlato) == 0

while not hotovo():
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))

    kam_lze_jit = chodby[hrac]
    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])

    if zlato[hrac] > 0:
        print("Moznost X : sebrat", zlato[hrac], "zlata")

    if hrac == klic:
        print("Moznost C : sebrat klíč")

    if ma_klic and zamcene_chodby[hrac]:
        print("Moznost R : odemknout dveře ->", mistnosti[zamcene_chodby[hrac][-1]])



    vstup_ok=False
    while not vstup_ok:
        vstup = input("> ")
        if not ma_klic and klic==hrac and vstup=="c":
            vstup_ok=True
        elif zlato[hrac] and vstup=="x":
            vstup_ok=True
        elif vstup=="r" and hrac==1 and zamcene_chodby[hrac]:
            vstup_ok=True
        elif je_cislo(vstup) and int(vstup)-1 <= len(kam_lze_jit):
            vstup_ok=True


    if vstup == "x":
        skore += zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "c":
        ma_klic = True
        klic = -1
    elif vstup == "r":
        cilova_mistnost = zamcene_chodby[hrac].pop()
        chodby[hrac].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
    else:
        hrac = kam_lze_jit[int(vstup) - 1]

    kroky += 1

print("Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")
