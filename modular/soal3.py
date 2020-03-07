def hargaitem(lel,aym,hati,tero,teh,jer):
    print("Lele Goreng/Bakar    ",lel,"x       ",lel * 10000)
    print("Ayam Goreng/Bakar    ", aym, "x       ", aym * 12000)
    print("Ampela Goreng/Bakar    ", hati, "x       ", hati * 4000)
    print("Terong Goreng/Bakar    ", tero, "x       ", tero * 6000)
    print("Teh Dingin/Panas    ", teh, "x       ", teh * 2500)
    print("jeruk Dingin/Panas    ", jer, "x       ", jer * 2500)
    print("-"*50,"+")
    return ((lel*10000)+(aym*12000)+(hati*4000)+(tero*6000)+(teh*2500)+(jer*2500))

print("="*15,"Selamat Datang","="*15)
print("Masukkan jumlah item sesuai dengan apa yang anda makan")
lele=int(input("Lele Goreng/Bakar: "))
Ayam=int(input("Ayam Goreng/Bakar: "))
Ampela=int(input("Ampela Goreng/Bakar: "))
Terong=int(input("Terong Goreng/Bakar: "))
Teh=int(input("Teh Dingin/Panas: "))
Jeruk=int(input("Teh Dingin/Panas: "))
print("="*15,"Nota Pecel Lele lali","="*15)
tot=hargaitem(lele,Ayam,Ampela,Terong,Teh,Jeruk)
print("Total            : ",tot)
if str(input("Ada kode promo? "))=="BAYARINTEMEN":
    print("Diskon           ",tot*0.1)
    print("Total setelah diskon         :",tot-(tot*0.1))
    bayar = int(input("Bayar            :"))
    if bayar<tot-(tot*0.1):
        print("Uang anda kurang")
    else:
        print("kembalian: ",bayar-tot(tot*0.1))
else:
    print("Diskon                       :0")
    print("Total setelah diskon         :",tot)
    bayar=int(input("Bayar                      :"))
    if bayar<tot:
        print("uang tidak cukup")
    else:
        print("kembalian: ",bayar-tot)
