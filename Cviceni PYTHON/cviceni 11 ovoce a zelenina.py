zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]
pocet_slov=0
pokracovat ="ano"
while pokracovat=="ano":
   slovo= input("Zadej název libovolného ovoce nebo zeleniny:\n")
   if slovo in ovoce:
        print("zadal jsi ovoce")
   elif slovo in zelenina:
        print("zadal jsi zeleninu")
   else:
        print("tvoje slovo nemám v seznamu")
    pocet_slov +=1
    pokracovat=input("Přeješ si zadat další slovo?(ANO/NE)")

