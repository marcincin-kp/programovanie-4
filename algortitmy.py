### ------------------------- 1 -------------------------

pole = ["apple", "42", "banana", "1700", "car", "88", "dog", "23", "99", "house", "guitar", "34", "island", "56", "78", "jungle", "flower", "65", "elephant", "91"]
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

### ------------------------- 2 -------------------------

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
    {"patient_id": 17, "first_name": "Tom", "last_name": "Halliwell", "gender": "M", "birth_date": "1987-08-01", "city": "Hamilton", "province_id": "ON", "allergies": "Ragweed", "height": 179, "weight": 114},
    {"patient_id": 19, "first_name": "John", "last_name": "West", "gender": "M", "birth_date": "1961-06-19", "city": "Oakville", "province_id": "ON", "allergies": None, "height": 138, "weight": 61},
    {"patient_id": 20, "first_name": "Jon", "last_name": "Doggett", "gender": "M", "birth_date": "1951-12-25", "city": "Hamilton", "province_id": "ON", "allergies": None, "height": 194, "weight": 116},
]


celkova_vaha = 0
for patient in patients_data:
    celkova_vaha += patient["weight"]
priemerna = celkova_vaha / len(patients_data)
print(priemerna)

celkova_vyska = 0
for patient in patients_data:
    celkova_vyska += patient["height"]
priemerna = celkova_vyska / len(patients_data)
print(priemerna)

### ------------------------- 3 -------------------------
import random
nahodne_cislo = random.randint(1, 100)
while int(input("cislo: ")) != nahodne_cislo:
    print("Netrafili ste.")

print("Trafili ste! Koniec hry")


### ------------------------- 3 - alternatíva (prehľadnejšie) -------------------------

import random
nahodne_cislo = random.randint(1, 100)
while True:
    tipnute_cislo = int(input("Zadajte číslo: "))
    if tipnute_cislo == nahodne_cislo:
        print("Trafili ste! Koniec hry")
        break
    else:
        print("Netrafili ste.")

### ------------------------- 4 -------------------------

pole = []

for x in range(4):
    pole.append(input("Zadajte prvok: "))

print(max(pole))
print(min(pole))

for x in range(4):
    print(x, pole[x])

### ------------------------- 5 -------------------------

import turtle
pero=turtle.Turtle()
def spirala(pocet_ciar, uhol, dlzka_strany):
    for x in range(pocet_ciar):
        pero.fd(dlzka_strany *x)
        pero.lt(uhol)
spirala(30,60,5)
spirala(20,30,3)

### ------------------------- 6 -------------------------

pole = [1,5,6,2,37,34,23,62,22,11]

print(pole)

c = pole[4]
pole[4] = pole[7]
pole[7] = c

print(pole)


### ------------------------- 7 -------------------------

pole = []
while True:
    pole.append(input("zadajte elementy:"))
    print(len(pole))
    if len(pole)== 9:
        print(pole)
        break


### ------------------------- 8 -------------------------

rok = int(input("Zadajte rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print("Prestupný rok.")
else:
    print("Neprestupný rok.")

### ------------------------- 9 -------------------------

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

### ------------------------- 10 -------------------------

cislo = int(input("Zadajte číslo od 1 po 100: "))

for x in range(1, cislo+1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)

### ------------------------- 11 -------------------------



### ------------------------- 12 -------------------------


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

### ------------------------- 13 -------------------------



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


### ------------------------- 14 -------------------------

def kalkulacka(cislo1, cislo2, operacia):
    if operacia == "+":
        return cislo1 + cislo2
    elif operacia == "-":
        return cislo1 - cislo2
    elif operacia == "*":
        return cislo1 * cislo2
    elif operacia == "/":
        if cislo2 == 0:
            print("Neplatná operácia")
        else:
            return cislo1 / cislo2

print(kalkulacka(2,3,"+"))
scitanie = kalkulacka(4,5,"+")
print(scitanie)

print(kalkulacka(11,0,"/"))

### ------------------------- 15 -------------------------

import random
import time
while True:
    hod_kockou = random.randint(1, 6)
    print(f"Hádžete...")
    time.sleep(1)
    print(f"Hodili ste: {hod_kockou}")
    if hod_kockou == 1:
        print("Smola!")
        break
    elif hod_kockou == 6:
        print("Vyhrali ste!")
        break
    else:
        odpoved = input("Smola! Chcete hádzať znovu? (y/n)")
        if odpoved == "y":
            continue
        else:
            print("Zrušili ste hru.")
            break

### ------------------------- 16 -------------------------
import turtle
t = turtle.Turtle()
t.speed(3)

def stvorec(dlzka):
    t.pensize(3)
    t.color("blue")
    for x in range(4):
        t.fd(dlzka)
        t.lt(90)

def schody(dlzka):
    for x in range(6):
        stvorec(dlzka)
        t.fd(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.rt(90)

    for x in range(6):
        t.bk(dlzka)
        t.lt(90)
        t.bk(dlzka)
        t.rt(90)

schody(50)
turtle.mainloop()

### ------------------------- 17 -------------------------

def nakup():
    nakup = []
    celkova_suma = 0
    while True:
        polozka = input("Zadajte položku: ")
        if polozka == "exit":
            print(nakup)
            print(celkova_suma)
            break
        cena = int(input("Zadajte cenu: "))
        nakup.append(polozka)
        celkova_suma += cena

nakup()

### ------------------------- 18 -------------------------
meno = input("Meno: ")
prezvisko = input("Prezvisko: ")
vek = input("Vek: ")
spolu = (f"{meno} {prezvisko} {vek}")
print(len(spolu))
print(spolu)

pocet_a = 0
for pes in spolu:
    if pes == "a":
        pocet_a += 1
print(f"Počet a v stringu: {pocet_a}")

### ------------------------- 19 -------------------------

def fast_food(pocet_hamb, pocet_hr, pocet_h):
    cena_hamb = 2.5
    cena_hr = 1.7
    cena_h = 1.9
    sucet = (pocet_hamb * cena_hamb) + (pocet_hr * cena_hr) + (pocet_h * cena_h)
    print(sucet)

fast_food(30,60,5)
fast_food(20,30,3)

### ------------------------- 20 -------------------------


pocet_pokusov = 3
while True:
    heslo = input("Zadajte heslo: ")

    if heslo == "tajne123":
        print("Prístup povolený")
    else:
        print("Nesprávne heslo.")
        pocet_pokusov -= 1
        if pocet_pokusov == 0:
            print("Prístup zablokovaný.")
            break
        else:
            print(f"Počet zostávajúcich pokusov: {pocet_pokusov}")
### ------------------------- 21 -------------------------
veta = input("Zadajte vetu:")

for pismeno in veta:
    if pismeno in ["e", "f", "b"]:
        print(f"Našli sme {pismeno}")
veta = veta.lower()
for samohlaska in ["a","e","i","o","u","y"]:
    veta = veta.replace(samohlaska, "")
print(veta)

### ------------------------- 22 -------------------------
text = input("Enter your text: ")

try:
    with open("vystup.txt", "a", encoding="utf-8") as subor:
        subor.write(text)
        print("Text bol vpísaný do súboru.")
except FileNotFoundError:
    print("Súbor sa nenašiel.")

### ------------------------- 23 -------------------------
n = int(input("Zadajte číslo n: "))
sucet = 0
for i in range(n):
    if i % 2 == 0:
        sucet += i
print(f"Súčet párnych čísel od 1 do {n} je: {sucet}")
### ------------------------- 24 -------------------------
list = []
while True:
    n = int(input("Enter a number: "))
    if n != 0:
        list.append(n)
    else:
        break

print(list)
sum = sum(list)
print(sum)
if len(list) != 0:
    print(sum/len(list))
### ------------------------- 25 -------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

multiplication = 0
for i in range(num1):
    multiplication += num2

print(multiplication)
### ------------------------- 26 -------------------------
import turtle
pero = turtle.Turtle()
pocet_stran = int(input("Koľko strán má tvoj viacuholník: "))

for i in range(pocet_stran):
    pero.forward(100)
    pero.right(360/pocet_stran)
turtle.mainloop()
### ------------------------- 27 -------------------------
import turtle
pero = turtle.Turtle()
while True:
    utvar = input("Zadaj útvar, ktorý chceš nakresliť: (štvorec, trojuholník, kruh)")

    if utvar not in ["štvorec", "trojuholník", "kruh"]:
        print("Neznámy tvar, skúste ešte raz.")
        continue

    os_x = int(input("Zadaj súradnicu x:"))
    os_y = int(input("Zadaj súradnicu y:"))
    pero.pu()
    pero.goto(os_x, os_y)
    pero.pd()

    if utvar == "štvorec":
        for x in range(4):
            pero.fd(50)
            pero.lt(90)
    if utvar == "trojuholník":
        for x in range(3):
            pero.fd(50)
            pero.lt(120)
    if utvar == "kruh":
        pero.circle(50)

turtle.mainloop()
### ------------------------- 28 -------------------------

### ------------------------- 29 -------------------------

try:
    with open("vystup.txt", "r", encoding="utf-8") as subor:
        obsah = subor.read()
        print(obsah)
        print(obsah.count("\n"))

except FileNotFoundError:
    print("Súbor sa nenašiel.")

### ------------------------- 30 -------------------------


