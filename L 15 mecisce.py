mesic = int(input("Vlož měsíc jako číslo\n"))
match (mesic):
    case 1 | 2 | 3:
        print("Je první čtvrtletí.")
    case 4 | 5 | 6:
        print("Je druhé čtvrtletí.")
    case 7 | 8 | 9:
        print("Je třetí čtvrtletí.")
    case 10 | 11 | 12:
        print("Je čtvrté čtvrtletí.")