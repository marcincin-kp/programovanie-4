from backend import *

def nemocnica():
    print("Vitajte v nemocnici, máte nasledujúce možnosti: ")
    print("1 - nájsť najvyššieho pacienta")
    print("2 - vyčisti alergickych")
    print("3 - nájsť doktora s najdlhším priezviskom")
    print("4 - nájsť najvyššieho doktora")
    volba = input("Zadajte možnosť: ")

    if volba == "1":
        najvyssi(patients_data)
    elif volba == "2":
        vycisti_alergickych(patients_data)
    elif volba == "3":
        clovek_s_naj_priezviskom(doctors_data)
    elif volba == "4":
        najvyssi(doctors_data)
    else:
        print("Skúste ešte raz, takáto možnosť neexistuje.")
    nemocnica()

nemocnica()
