s=input("souhlasky nebo samohlasky?")
while not (s=="samohlasky" or  s=="souhlasky" or  s=="nic"):
    s=input("souhlasky nebo samohlasky?")

napis=input("napis neco:")
pocet_samohlasek=0
pocet_souhlasek=0
pocet_mezer=0
for i in napis:
    if i == 'a' or i== "e" or i== "o" or i== "u" or i=="i" or i=="y" or i == 'A' or i== "E" or i== "O" or i== "U" or i=="I" or i=="Y" or i == "ě" or i == "ý" or i == "Ý" or i == "Ě" or i == "é" or i == "É" or i == "í" or i == "Í" or i == "á" or i == "Á":
        if s=="samohlasky":
            print(i)
        pocet_samohlasek=pocet_samohlasek+1
    else:
        if not i == " ":
            if s=="souhlasky":
                print(i)
            pocet_souhlasek=pocet_souhlasek+1
        else:
            pocet_mezer=pocet_mezer+1



print("počet souhlásek:",(pocet_souhlasek))
print("počet samohlásek:",(pocet_samohlasek))
print("počet mezer:",pocet_mezer)
print("pocet pismen:", pocet_souhlasek+pocet_samohlasek)
print("počet všech znaků",pocet_mezer+pocet_souhlasek+pocet_samohlasek)

