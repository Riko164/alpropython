def hapus_sebelahsama(string):
    tamp=""
    for i in range(0,len(string)):
        if i==0:
            tamp+=string[i]
        elif string[i]!=string[i-1]:
            tamp+=string[i]
    return tamp
