def rekursif(angka):
    if angka==0 or angka==1:
        return angka
    else:
        return rekursif(angka-1)+rekursif(angka-2)

bilangan=int(input("Masukkan bilangan: "))
for i in range(0,bilangan):
    if rekursif(i)>bilangan:
        break
    else:
        print(rekursif(i), end=" ")
