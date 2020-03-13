angka=int(input("input bilangan: "))
counter1=0
counter2=angka*4-2
for i in range(0,angka*2):
    for j in range(0,angka*4-1):
        if i==0:
            print("*", end='')
        elif j==counter1 or j==counter2:
            print("*",end='')
        else:
            print(" ",end='')
    print("")
    counter1+=1
    counter2-=1
