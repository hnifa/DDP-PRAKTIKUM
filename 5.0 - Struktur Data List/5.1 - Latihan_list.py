#dalam python index diawali 0 (nol)
#ar = array
ar_buah = ['Pepaya', 'Mangga', 'Pisang', 'Jambu', 'Belimbing']

#mengganti index [2] dengan Apel
ar_buah [2] = 'Apel'

#menghapus index [4]
del ar_buah [4]

#print buah index [2]
print('Buah index ke-2: ', ar_buah[2])

#cetak all elements list
for buah in ar_buah:
    print('Buah', buah)

#menambahkan di paling belakang (append)
ar_buah.append('Semangka')

#menambahkan di posisi yang diinginkan (insert)
ar_buah.insert(2, 'Melon') 

##cetak all elements list
for buah in ar_buah:
    print('Buah', buah)

huruf = ['a', 'b', 'c', 'd', 'e', 'f']

#memotong list 
print('Memotong List huruf index 1-5:', huruf [1:5])
print('Memotong List huruf index 2-4:', huruf [2:4])
