def cek_kembali(bilangan):
    kata=str(bilangan)
    tot=0
    for i in range(0,len(kata)):
        tot+=int(kata[i])**len(kata)
    if tot==bilangan:
        return True
    else:
        return False
print(cek_kembali(370))
