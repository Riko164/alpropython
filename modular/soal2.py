def hitungtanggal(tgl,bln,thn):
    if tgl==0 and bln==0 and thn==0:
        print("="*60)
        print("Sehari juga bisa kekumpul Rp. 50000 kan pak")
    elif tgl>=0 and bln>=0 and thn>=0:
        print("=" * 60)
        print("Wah, ternmyata butuh ",thn," Tahun ",bln," Bulan ",tgl," Hari")
        print("Untuk mengumpukan uang receh sebanyak Rp. 50000")
    else:
        print("=" * 60)
        print("Tanggal nya kok mundur?")
try:
    print("="*20,"Selamat Datang Pak Ogah","="*20)
    Tglper=int(input("Masukkan tanggal pertama: "))
    Blnper=int(input("Masukkan bulan pertama: "))
    Thnper=int(input("Masukkan tahun pertama: "))
    Tglper=int(input("Masukkan tanggal kedua: "))-Tglper
    Blnper=int(input("Masukkan bulan kedua: "))-Blnper
    Thnper=int(input("Masukkan tahun kedua: "))-Thnper
    hitungtanggal(Tglper,Blnper,Thnper)
except:
    print("Input salah")
