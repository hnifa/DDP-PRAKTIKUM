# Dictionary menggunakan kurung kurawal {} 
# {'a':b}    a = keys dan b = values 
# %s = string,  %i = integer

#1
nilai = {'Aslam':80, 'Farida':85, 'Hanifa':90, 'Novita':90}
print("Data nilai : ",nilai)

#2
print("\n---cetak valuenya saja---\n")
for skor in nilai.values():
    print("Data Nilai : ",skor)

#3
print("\n---cetak key saja---\n")
for nama in nilai.keys():
    print("Data Siswa : ",nama)

#4
print("\n---cetak key dan values---\n")
for nama,skor in nilai.items():
    print("Nama Siswa : %s \t Nilai : %i" % (nama,skor))


#Cara menghapus nilai Aslam
nilai.pop('Aslam')

#Cara menghapus nilai Novita
del nilai['Novita']
