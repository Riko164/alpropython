angka=int(input("Masukan bilangan: "))
for i in range(0,angka):
    for j in range(1,angka+1):
        j+=i
        if j>angka:
            print(j-angka,end='')
        else:
            print(j,end='')
    print("")
