nama = "Hanifa"
mapel = "Matematika"
nilai = 80.00

#elif = pilihan lain dan else = jika tidak ada yang tepat
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai <=85):
    grade = "B"
elif(nilai >= 60 and nilai <=75):
    grade = "C"
elif(nilai >= 30 and nilai <= 60):
    grade = "D"
else:
    grade = "E"

print("Nama Siswa \t:",nama, 
    "\nMata Pelajaran \t:",mapel, 
    "\nNilai \t\t:",nilai, 
    "\nGrade \t\t:",grade)