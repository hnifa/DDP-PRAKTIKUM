#def adalah kata kunci

def hitung_gaji():
    nama = input('Nama\t\t: ')
    jabatan = input('Jabatan\t\t: ')
    agama = input('Agama\t\t: ')
    jumlah = int(input('Jumlah Anak\t: '))

    def gapok(jabatan):
        return{
            'General Manager' : 20000000,
            'Manager' : 10000000,
            'Staff' : 5000000
        }[jabatan]
    
    persen = 0.01 
    if(jumlah > 0 and jumlah <4):
        tunak = gapok(jabatan) * persen * jumlah
    elif(jumlah > 3):
        tunak = gapok(jabatan) * persen * (jumlah-(jumlah-3))
    else:
        tunak = 0

    gaji_kotor = gapok(jabatan) + tunak
    zakat = (0, 0.025 * gaji_kotor) [agama == 'islam' or 'Islam' and gaji_kotor >= 6000000]
    gaber = (gapok(jabatan) + tunak) - zakat

    print('\n\n---Data Pegawai---'
        '\nNama Pegawai\t\t:',nama,
        '\nJabatan\t\t\t:',jabatan,
        '\nAgama\t\t\t:',agama,
        '\nJumlah Anak\t\t:',jumlah,
        '\nGaji Pokok\t\t:',gapok(jabatan),
        '\nTunjangan Keluarga\t:',tunak,
        '\nZakat Profesi\t\t:',zakat,
        '\nTake Home Pay\t\t:',gaber
    )

print('\n\n---Input Pegawai---')
hitung_gaji()

        