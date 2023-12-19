mistonsti=["obyvak","chodba","sklep","truni sal"]
chodby=[[1,2],[0],[0],[1,2]]
zamcene_chodby= [[],[3],[],[]]
klic=2


hracova_pozice=0
zlato=[1,0,10,300]
hracovo_zlato=0
kroky=0
mam_klic=False
def hotovo():
        return sum(zlato) == 0
while not hotovo():
    print(" ")
    print("hrac je v mistnosti ",mistonsti[hracova_pozice],end=" ")
    print("a ma",hracovo_zlato,"zlata")
    print("zbyva zlata:",sum(zlato))
    kam_lze_jit=chodby[hracova_pozice]
    for i, moznost in enumerate (kam_lze_jit):
        print("moznost jit",i+1,":", mistonsti[moznost])
    if zlato[hracova_pozice] > 0:
        print("je tu zlato!!!")
        print("moznost x: sebrat", zlato[hracova_pozice],"zlata")

    if hracova_pozice == klic and not mam_klic:
        print("moznost c:sebrat klic")
    vstup = input(">")

    if vstup == "x":
        hracovo_zlato += zlato[hracova_pozice]
        zlato[hracova_pozice]=0
    elif vstup == "c" and not mam_klic:
        mam_klic=True
    else:
        index_moznosti = int(vstup) -1
        hracova_pozice = kam_lze_jit[index_moznosti]
    kroky+=1















print("VYHRAL JSI za",kroky,"kroku")
