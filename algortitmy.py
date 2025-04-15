
meno = input("Meno: ")
prezvisko = input("Prezvisko: ")
vek = input("Vek: ")
spolu = (f"{meno} {prezvisko} {vek}")
print(len(spolu))
print(spolu)

def fastfood(ham, hra, hot):
    vsetko = (ham*2.5) + (hra*1.7) + (hot*1.9)
    print(vsetko)
fastfood(2,3,6)

import random
cislo = random.randint(1, 100)
while int(input("cislo: "))!=cislo:
    print("netrafily ste")

print("koniec hry")

pole = []

for x in range(4):
    pole.append(input("Zadajte prvok: "))

print(max(pole))
print(min(pole))

for x in range(4):
    print(x, pole[x])

import random

nahodne_cislo = random.randint(1, 10)

while nahodne_cislo != int(input("Tipnite si číslo: ")):
    print("Nesprávne číslo, skúste ešte raz.")
print("Trafili ste číslo.")

rok = int(input("Zadajte rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print("Prestupný rok.")
else:
    print("Neprestupný rok.")




pole = []
while True:
    pole.append(input("zadajte elementy:"))
    print(len(pole))
    if len(pole)== 9:
        print(pole)
        break




pole = [
    "apple",
    "42",
    "banana",
    "1700",
    "car",
    "88",
    "dog",
    "23",
    "99",
    "house",
    "guitar",
    "34",
    "island",
    "56",
    "78",
    "jungle",
    "flower",
    "65",
    "elephant",
    "91"
]
polec = []
poles = []

for element in pole:
    if element.isdigit():
        polec.append(element)
    else:
        poles.append(element)
poles.sort()
polec.sort()
print(poles)
print(polec)

knihy = [
    {"nazov": "1984", "autor": "George Orwell", "rok": 1949},
    {"nazov": "Sto rokov samoty", "autor": "Gabriel García Márquez", "rok": 1967},
    {"nazov": "Zločin a trest", "autor": "Paulo Coelho", "rok": 1866},
    {"nazov": "Pýcha a predsudok", "autor": "Jane Austen", "rok": 1813},
    {"nazov": "Veľký Gatsby", "autor": "Paulo Coelho", "rok": 1925},
    {"nazov": "Na ceste", "autor": "Jack Kerouac", "rok": 1957},
    {"nazov": "Meno ruže", "autor": "Umberto Eco", "rok": 1980},
    {"nazov": "Mechanický pomaranč", "autor": "Anthony Burgess", "rok": 1962},
    {"nazov": "Farma zvierat", "autor": "George Orwell", "rok": 1945},
    {"nazov": "Malý princ", "autor": "Antoine de Saint-Exupéry", "rok": 1943},
    {"nazov": "Lovec v žite", "autor": "J.D. Salinger", "rok": 1951},
    {"nazov": "To", "autor": "Stephen King", "rok": 1986},
    {"nazov": "Biely tesák", "autor": "Jack London", "rok": 1906},
    {"nazov": "Alchymista", "autor": "Paulo Coelho", "rok": 1988},
    {"nazov": "Hobit", "autor": "J.R.R. Tolkien", "rok": 1937}
]


meno_autora = input("Zadajte meno autora: ")
pole_knih = []

for kniha in knihy:
    if kniha["autor"] == meno_autora:
        pole_knih.append(kniha["nazov"])

if len(pole_knih) == 0:
    print("Autor nemá knihy v databáze.")

for kniha in pole_knih:
    print(kniha)

cislo = int(input("Zadajte cislo: "))

if cislo == 0:
    print("Zadali ste nula.")
elif cislo > 0:
    if cislo % 2 == 0:
        print("Číslo je párne a kladné.")
    else:
        print("Číslo je nepárne a kladné.")
elif cislo < 0:
    if cislo % 2 == 0:
        print("Číslo je párne a záporné.")
    else:
        print("Číslo je nepárne a záporné.")


patients_data = [
    {"patient_id": 1, "first_name": "Donald", "last_name": "Waterfield", "gender": "M", "birth_date": "1963-02-12", "city": "Barrie", "province_id": "ON", "allergies": None, "height": 156, "weight": 65},
    {"patient_id": 2, "first_name": "Mickey", "last_name": "Baasha", "gender": "M", "birth_date": "1981-05-28", "city": "Dundas", "province_id": "ON", "allergies": "Sulfa", "height": 185, "weight": 76},
    {"patient_id": 3, "first_name": "Jiji", "last_name": "Sharma", "gender": "M", "birth_date": "1957-09-05", "city": "Hamilton", "province_id": "ON", "allergies": "Penicillin", "height": 194, "weight": 106},
    {"patient_id": 4, "first_name": "Blair", "last_name": "Diaz", "gender": "M", "birth_date": "1967-01-07", "city": "Hamilton", "province_id": "ON", "allergies": None, "height": 191, "weight": 104},
    {"patient_id": 5, "first_name": "Charles", "last_name": "Wolfe", "gender": "M", "birth_date": "2017-11-19", "city": "Orillia", "province_id": "ON", "allergies": "Penicillin", "height": 47, "weight": 10},
    {"patient_id": 7, "first_name": "Thomas", "last_name": "ONeill", "gender": "M", "birth_date": "1993-01-31", "city": "Burlington", "province_id": "ON", "allergies": None, "height": 180, "weight": 117},
    {"patient_id": 8, "first_name": "Sonny", "last_name": "Beckett", "gender": "M", "birth_date": "1952-12-11", "city": "Port Hawkesbury", "province_id": "NS", "allergies": None, "height": 174, "weight": 105},
    {"patient_id": 10, "first_name": "Cedric", "last_name": "Coltrane", "gender": "M", "birth_date": "1961-11-10", "city": "Toronto", "province_id": "ON", "allergies": None, "height": 157, "weight": 61},
    {"patient_id": 11, "first_name": "Hank", "last_name": "Spencer", "gender": "M", "birth_date": "1969-08-10", "city": "Peterborough", "province_id": "ON", "allergies": None, "height": 158, "weight": 74},
    {"patient_id": 14, "first_name": "Rick", "last_name": "Bennett", "gender": "M", "birth_date": "1977-01-27", "city": "Ancaster", "province_id": "ON", "allergies": "Penicillin", "height": 220, "weight": 95},
    {"patient_id": 16, "first_name": "Woody", "last_name": "Bashir", "gender": "M", "birth_date": "1951-11-15", "city": "Barrie", "province_id": "ON", "allergies": "Penicillin", "height": 153, "weight": 59},
    {"patient_id": 17, "first_name": "Tom", "last_name": "Halliwell", "gender": "M", "birth_date": "1987-08-01", "city": "Hamilton", "province_id": "ON", "allergies": "Ragweed", "height": 231, "weight": 114},
    {"patient_id": 19, "first_name": "John", "last_name": "West", "gender": "M", "birth_date": "1961-06-19", "city": "Oakville", "province_id": "ON", "allergies": None, "height": 138, "weight": 61},
    {"patient_id": 20, "first_name": "Jon", "last_name": "Doggett", "gender": "M", "birth_date": "1951-12-25", "city": "Hamilton", "province_id": "ON", "allergies": None, "height": 194, "weight": 116},
]
meno_najvyssieho = ""
priezvisko_najvyssieho = ""
vyska_najvyssieho = 0

for patient in patients_data:
    if patient["height"] > vyska_najvyssieho:
        vyska_najvyssieho = patient["height"]
        meno_najvyssieho = patient["first_name"]
        priezvisko_najvyssieho = patient["last_name"]

print(f"Najvyšší pacient je {meno_najvyssieho} {priezvisko_najvyssieho} a je vysoký {vyska_najvyssieho}")
