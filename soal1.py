counter=0
try:
    bawah = int(input("Masukkan Batas Bawah: "))
    atas = int(input("Masukkan Batas Atas: "))
except:
    counter=1
if counter==1 or bawah>atas:
    print("Salah Inputan")
else:
    print("Angka Genap dari angkas",bawah," sampai ",atas," adalah ", end='')
    for i in range(bawah,atas):
        if i%2 == 0 and i!=bawah :
            print(i,end=' ')

