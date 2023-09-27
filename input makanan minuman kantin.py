print("selamat datang di kantin trisakti")
print("1.nasi telur = 10.000")
print("2.nasi orak arik = 15.000")
print("3.bakso = 15.000")

pilihan1 = input("pilih makanan: ")
total = 0

if ("1.nasi telur" in pilihan1):
    total += 10
elif ("2.nasi orak arik" in pilihan1):
    total += 15
elif ("3.bakso" in pilihan1):
    total += 15

print("\n")
print("1.es teh = 5.000")
print("2.teh tawar = 7.000")
print("3.es teler = 10.000")

pilihan2 = input("pilih minuman: ")

if ("1.es teh" in pilihan2):
    total += 5
elif ("2.teh tawar" in pilihan2):
    total += 7
elif ("3.es teler" in pilihan2):
    total += 10

if total > 0:
    print(total)