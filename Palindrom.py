palindrom=input("Zadej palindrom:\n")
pozpatku=palindrom[::-1]
if palindrom==pozpatku:
    print("Ano, je to palindrom")
else:
    print("Ne, není to palindrom")

