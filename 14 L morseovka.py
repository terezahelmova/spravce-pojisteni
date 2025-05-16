print("Zadejte zprávu k zakódování: ")

puvodni_zprava = input().lower()
zasifrovana_zprava = ""

# vzorová pole
abeceda = "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                  "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                  ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

for znak in puvodni_zprava:
    pozice = abeceda.find(znak)
    if pozice >= 0:
        zasifrovana_zprava += morseovy_znaky[pozice] + " "

print(f"Zakódovaná zpráva: {zasifrovana_zprava}")

