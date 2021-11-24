## %s = "a" string
# %i = integer
# %d = decimal
# %03d = 001 (desimal dengan 3 digit)
# %f = float
# %.2f = 1.00 (float dengan 2 digit di belakang koma) 

print('\n---luas bidang----\n')
print('Pilih Bidang: '
    '\n1.Lingkaran'
    '\n2.Segitiga'
    '\n3.Persegi Panjang'
    )

pilihan = int(input('Pilih No. Bidang: '))
if (pilihan == 1):
    bidang = 'Lingkaran'
    jari2 = float(input('Masukkan jari2: '))
    luas = 3.14 * jari2 * jari2

print('Bidang %s dengan jari2 %.2f luasnya = %.2f' % (bidang,jari2,luas))