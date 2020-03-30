def replace_substring(awal, akhir, string, pengganti):
    temp=""
    counter=0
    for i in range(0,len(string)):
        if i < awal or i >akhir:
           temp+=string[i]
        elif counter==0:
            temp+=pengganti
            counter+=1
    return temp
