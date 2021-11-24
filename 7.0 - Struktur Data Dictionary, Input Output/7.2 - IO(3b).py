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
#logic
if (pilihan == 1):
    bidang = 'Lingkaran'
    jari2 = float(input('Masukkan jari2: '))
    luas = 3.14 * jari2 * jari2
    print('Bidang %s dengan jari2 %.2f luasnya = %.2f' 
    % (bidang,jari2,luas))

elif (pilihan == 2):
    bidang = 'segitiga'
    alas = float(input('Masukkan Alas: '))
    tinggi = float(input('Masukkan Tinggi: '))
    luas = 0.5 * alas * tinggi
    print('Bidang %s dengan alas %.2f dan tinggi %.2f luasnya = %.2f'
    % (bidang,alas,tinggi,luas))

elif (pilihan ==3):
    bidang = 'Persegi Panjang'
    p = float(input('Masukkan Panjang: '))
    l = float(input('Masukkan Lebar: '))
    luas = p * l
    print('Bidang %s dengan panjang %.2f dan lebar %.2f luasnya = %.2f'
    % (bidang,p,l,luas))

else:
    print('No. Bidang yang Anda pilih tidak ada')