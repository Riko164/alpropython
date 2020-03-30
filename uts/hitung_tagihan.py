def hitung_tagihan(golongan, pemakaian):
    if golongan==1:
        return 1000*pemakaian
    elif golongan==2:
        if pemakaian>100:
            return (1400*100)+((pemakaian-100)*2000)
        else:
            return 1400*pemakaian
    else:
        if pemakaian*2500 > 500000:
            return (pemakaian*2500)+((pemakaian*2500)*0.5)
        else:
            return pemakaian*2500
