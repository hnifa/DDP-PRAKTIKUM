a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('*', end = ' ') #end adalah jarak antara bintang
    a -= 1
    print ('')