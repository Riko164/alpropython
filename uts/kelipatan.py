def cetak(awal, akhir, kelipatan):
    for i in range(awal,akhir+1):
        if i%kelipatan!=0:
            print(i)

cetak(10, 20, 3)
