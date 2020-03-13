angka=int(input("input bilangan: "))
counter1=angka*2-1
counter2=counter1
for i in range(0,angka*2):
    for j in range(0,angka*4-1):
        if i==angka*2-1:
            print("*", end='')
        elif j==counter1 or j==counter2:
            print("*",end='')
        else:
            print(" ",end='')
    print("")
    counter1+=1
    counter2-=1
