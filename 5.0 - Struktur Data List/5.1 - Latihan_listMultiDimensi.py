#list dua dimensi
daftar_makanan = [
    ['bakwan', 'risol', 'pastel'],
    ['bakso', 'soto', 'sate'],
    ['cilok', 'cireng', 'cimol']
]
print('------cetak per item-------')
print(daftar_makanan[0][0])
print(daftar_makanan[1][1])
print(daftar_makanan[2][0])

print('----cetak all item nested looping------')
for menu in daftar_makanan:
    for makanan in menu:
        print(makanan)