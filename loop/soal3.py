kaset=0
buku=0
pilihan=1

def printmenu():
    print("<---Selamat data di Toko Sewa Sinar Kebenaran--->")
    print("Voucher diskon melakukan sewa : pahlawanKesiangan (Potongan 50%)")
    print("Pilihan :")
    print(" 1. Sewa Kaset")
    print(" 2. Sewa Buku")
    print(" 3. Total Harga")
    print(" 4. Exit")
    pilihan=int(input("Masukkan Pilihan: "))
    return pilihan

while pilihan>0:
    pilih=printmenu()
    if pilih==1:
        print("Peminjaman per kaset: Rp. 5000")
        kaset+=int(input("Banyaknya kaset yang dipinjam: "))
        if kaset<0:
            print("input yang bener bambang")
        else:
            input("Press Enter to continue")
    elif pilih==2:
        print("Peminjaman per buku: Rp. 10000")
        buku+=int(input("Banyaknya buku yang ingin dipinjam :"))
        if buku<0:
            print("input yang bener bambang")
        else:
            input("Press Enter to continue")
    elif pilih==3:
        print("Total harga sewa Rp. ",((kaset*5000)+(buku*10000)))
        tanya1=str(input("Mau langsung baya (Y/N) ?"))
        if tanya1=='y' or tanya1=='Y':
            tanya2=str(input("Gunakan vouvher (Y/N) ?"))
            if tanya2 == 'y' or tanya2=='Y':
                voucher=str(input("Masukkan kode voucher: "))
                if voucher=="pahlawanKesiangan":
                    print("total harga sewa menjadi Rp. ",((kaset*5000)+(buku*10000))/2)
                    kaset = 0
                    buku = 0
                else:
                    print("Kode yang dimasukkan salah :( , ulangi proses dari awal :)")
            else:
                print("total harga sewa menjadi Rp. ", ((kaset * 5000) + (buku * 10000)))
                kaset = 0
                buku = 0
    elif pilih==4:
        print("Terima Kasih telah berkunjug :D")
        break
    else:
        print("input yang benar bambang")
