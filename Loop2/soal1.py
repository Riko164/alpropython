def cek(angka):
    counter=0
    for i in range(2,angka):
        if(angka%i==0):
            counter=1

    if(counter==0):
        return True
    else:
        return False


banyak=int(input("Masukkan bilangan: "))
for i in range (2,banyak):
    if cek(i):
        print(i, end=" ")
