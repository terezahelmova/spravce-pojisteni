jmeno = input("Zadej své jméno:")
if not (len(jmeno)>=3 and len(jmeno)<=10):
    print("Máš moc krátké nebo moc dlouhé jméno!")
else: print("Normální jméno")