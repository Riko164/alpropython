bilangan=int(input("Masukkan bilangan: "))
if bilangan>2:
    for i in range(0,bilangan):
        for j in range(0,bilangan):
            if i==0 and j==0:
                print("#",end=" ")
            elif i==0:
                print("###",end=' ')
            elif i==bilangan-1 and j==bilangan-1:
                print("##",end=' ')
            elif i==bilangan-1:
                print("###", end=" ")
            elif j==bilangan-1:
                print("# ",end='')
            else:
                print("# #",end=" ")
        print("")
else:
    print("minimal 2")
