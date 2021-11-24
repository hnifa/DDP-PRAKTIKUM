#def adalah key word 

def hitung_umur (tahun_ini):
    nama = input('Nama Siswa : ')
    tahun_lahir = int(input('Tahun Lahir : '))
    umur = tahun_ini - tahun_lahir
    print("Siswa dengan nama %s yang lahir pada tahun %i berumur %.2f" % (nama,tahun_lahir,umur))

print('Data diri anda')
hitung_umur(2021)