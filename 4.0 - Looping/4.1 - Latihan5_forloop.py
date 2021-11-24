print ("------cetak angka 1 - 20-------")
angka = 20 
for no in range(angka):
    no += 1 # no = no + 1
    print("Angka", no)

print ("------cetak bil genap diantara 1 - 20-------")
angka = 20 
for no in range(angka):
    no += 1 # no = no + 1
    if(no % 2 == 0):
        print("Bil. genap", no)

print ("------cetak bil ganjil diantara 1 - 20-------")
angka = 20 
for no in range(angka):
    no += 1 # no = no + 1
    if(no % 2 == 1):
        print("Bil. ganjil", no)