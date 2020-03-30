def hitung_nilai(tugas1, tugas2, tugas3, tugas4, ujian):
    a=(tugas1+tugas2+tugas3+tugas4)/4
    if (ujian*0.6)+(0.4*a) > 55:
        print("Lulus")
    else:
        print("Tidak Lulus")
