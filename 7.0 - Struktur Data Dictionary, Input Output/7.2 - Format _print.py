# %s = "a" string
# %i = integer
# %d = decimal
# %03d = 001 (desimal dengan 3 digit)
# %f = float
# %.2f = 1.00 (float dengan 2 digit di belakang koma)  


#1
a = 'Nurul'
b = 'Fikri'
print('Saya belajar di',a,b) #memasukkan fungsi dipisahkan dengan koma

#2
lokasi = 'Nurul Fikri'
nama_jalan = 'Lenteng Agung'
nomor = 20
print('Jln. %s no. %i, %s' %(nama_jalan,nomor, 'Jakarta Selatan'))

#3
lat = -6.3529481
long = 106.8303389
print('Lokasinya di %.4f, %.4f' % (lat,long))