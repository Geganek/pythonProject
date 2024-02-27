import random
from lokace import Hrad,Posta
inventar = {"klic" : False, "moje zlato":0,"burger":False,"houbicka" : False}
sytost=4
kroky = 0
dedecek_us_rekl=False

hrad=Hrad()
posta=Posta()
def je_cislo(mozna_cislo):
    try:
        int(mozna_cislo)
        return True
    except ValueError:
        return False
def hotovo(level):
    return sum(level.zlato) == 0


for level in [Hrad,Posta]:
    hrac = 0

    print("vytej v levelu",level.jmeno)
    while not hotovo(level):
        print("mas sytost",sytost)
        if inventar["burger"]:
            print("mas burger")
        print("hráč je v místnosti:", level.mistnosti[hrac])
        print("hráč má", inventar["moje zlato"], "zlata")
        print("zbývá zlata:", sum(level.zlato))
        kam_lze_jit = level.chodby[hrac]
        ok_vstupy=[]

        if hrac == 5 and inventar["moje zlato"]>=5 and not inventar["houbicka"]:
            if not dedecek_us_rekl:
                print("jsem moudry dedecek a dam ti houbicky kdyz uhodnes cislo od 1 do 10 a das mi 5 kc")
                cislo=random.randint(1,10)
                inventar["moje zlato"]-=5
                dedecek_us_rekl=True

            while True:
                rekni_dedeckovi=input("cislo:")
                if je_cislo(rekni_dedeckovi):
                    dolnihranice=0
                    hornihranice=11
                    kroky=0

                if int(rekni_dedeckovi) == cislo:
                    print("mas houbicku")
                    break
                elif int(rekni_dedeckovi) > cislo:
                    print("mislim si mensi cislo")
                    hornihranice=(((hornihranice-dolnihranice)//2)+dolnihranice)
                else:
                    print("mislim si veci cislo")
                    dolnihranice=(((hornihranice-dolnihranice)//2)+dolnihranice)
                dedecek_us_rekl=False
        for i, moznost in enumerate(kam_lze_jit):
            print("Moznost", i + 1, ": ", level.mistnosti[moznost])
            ok_vstupy.append(str(i+1))
        if level.zlato[hrac] > 0:
            print("Moznost X : sebrat", level.zlato[hrac], "zlata")
            ok_vstupy.append("x")
        if hrac == level.mistnost_s_klicem:
            print("Moznost C : sebrat klíč")
            ok_vstupy.append("c")
        if inventar["klic"] and level.zamcene_chodby[hrac]:
            print("Moznost R : odemknout dveře ->", level.mistnosti[level.zamcene_chodby[hrac][-1]])
            ok_vstupy.append("r")
        if hrac == 4 or inventar["burger"]:
            print("moznost J: najíst se")
            ok_vstupy.append("j")
        if hrac == 4 and inventar["moje zlato"] >= level.cena_burgeru and not inventar["burger"]:
            print("prodavačka říká:Chceš burger?řekni b")
            ok_vstupy.append("b")


        vstup = input("> ")
        while not vstup in ok_vstupy:
            print("vyber nejakou moznost malymy pismeny:")
            for i in range(len(ok_vstupy)):
                print(ok_vstupy[i])
            vstup = input("> ")
        if vstup == "x":
            inventar["moje zlato"] += level.zlato[hrac]
            level.zlato[hrac] = 0
        elif vstup == "c":
            inventar["klic"] = True
            mistnost_s_klicem = -1
        elif vstup=="j":
            sytost=11

            if not hrac==4:
                inventar["burger"]=False
        elif vstup == "b":
            inventar["burger"]=True
            inventar["moje zlato"]-=level.cena_burgeru
        elif vstup == "r":
            cilova_mistnost = level.zamcene_chodby[hrac].pop()
            inventar["klic"]=False
            level.chodby[hrac].append(cilova_mistnost)
            print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
        else:
            hrac = kam_lze_jit[int(vstup) - 1]

        sytost-=1
        kroky += 1
        if sytost == 0:
            print("umřels hlady")
            break

    print("level",level.jmeno,"splnen")
print("Gratuluju, sebral jsi celkem,", inventar["moje zlato"], "zlata za", kroky, "kroků")
