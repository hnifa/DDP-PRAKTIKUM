nama1 = 'Hanifa'
nama2 = 'Budi'
mapel = 'Matematika'
nilai1 = 90.99
nilai2 = 55.55 

# cara if
if(nilai1,nilai2 >= 60):
     ket = 'lulus'
else:
     ket = 'gagal'
print('Hanifa dinyatakan', ket)
 
#tuple&list
ket = ('gagal', 'lulus') [nilai1 >= 60] #dituliskan false dulu baru true
print('Nama Siswa\t:', nama1,
      '\nMata Pelajaran\t:', mapel,
      '\nNilai\t\t:', nilai1,
      '\nKeterangan\t:', ket,
      '\n'
)

ket = ('gagal', 'lulus') [nilai2 >= 60] 
print('Nama Siswa\t:', nama2,
    '\nMata Pelajaran\t:', mapel,
    '\nNilai\t\t:', nilai2,
    '\nKeterangan\t:', ket
)