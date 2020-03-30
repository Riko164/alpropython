def tiga_tengah(string):
    if len(string)%2!=0:
        tengah=int(len(string)/2)
        print(string[tengah-1]+string[tengah]+string[tengah+1])
    else:
        print("Tidak memenuhi syarat")
