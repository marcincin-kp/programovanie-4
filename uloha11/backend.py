from db import *

def najvyssi(zoznam):
    naj_vyska = 0
    naj_clovek = {}
    for clovek in zoznam:
        if clovek["height"] > naj_vyska:
            naj_vyska = clovek["height"]
            naj_clovek = clovek
    print(f"naj_clovek: {naj_clovek["first_name"]}")

def vycisti_alergickych(zoznam):
    pole_nepohode = []
    for pacient in zoznam:
        if pacient["allergies"] != None:
            pole_nepohode.append(pacient)
    for alergicky_pacient in pole_nepohode:
        zoznam.remove(alergicky_pacient)
    for pacient in zoznam:
        print(f"pacient: {pacient}")

def clovek_s_naj_priezviskom(zoznam):
    dlzka_priezviska = 0
    naj_priezvisko = ""
    naj_clovek = {}
    for clovek in zoznam:
        if len(clovek["last_name"]) > dlzka_priezviska:
            dlzka_priezviska = len(clovek["last_name"])
            naj_clovek = clovek
            naj_priezvisko = clovek["last_name"]
    print(f"Najdlhšie priezvisko je: {naj_priezvisko} a patrí {naj_clovek}")

