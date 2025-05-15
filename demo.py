veta = input("Zadajte vetu:")

for pismeno in veta:
    if pismeno in ["e", "f", "b"]:
        print(f"Našli sme {pismeno}")
veta = veta.lower()
for samohlaska in ["a","e","i","o","u","y"]:
    veta = veta.replace(samohlaska, "")
print(veta)