def create_sword(leaf, mushroom, chicken):
    potion=0
    sword=0
    while(leaf >=10 or mushroom>=7):
        if potion>=5 and chicken>=2 and leaf>=10:
           sword+=1
           potion-=5
           chicken-=2
           leaf-=10
        else:
            if leaf-5 >= 0 and mushroom-7 >= 0:
                potion+=1
                leaf-=5
                mushroom-=7
            else:
                break
    return sword

print(create_sword(35, 35, 2))
