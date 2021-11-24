## %s = "a" string
# %i = integer
# %d = decimal
# %03d = 001 (desimal dengan 3 digit)
# %f = float
# %.2f = 1.00 (float dengan 2 digit di belakang koma) 

print('---perkalian---')
angka = float(input("Masukkan angka: "))
hasil = 10 * angka
print("Perkalian 10 x",angka,"=",hasil) #cara biasa
print("Perkalian 10 x %.2f = %.2f" % (angka,hasil)) #menggunakan format print