tot=0
semester=int(input("Masukkan semester anda saat ini: "))
ipssemster=""

for i in range(0,semester):
    print("IPS anda pada semster ",(i+1)," adalah: ",end='')
    ips=float(input())
    tot += ips
    ipssemster+="IPS anda pada semster "+str(i+1)+" adalah: "+str(ips)+","

temp= ipssemster.split(",")
for i in temp:
    print(i)

print("Sehingga IPK anda adalah ",tot/semester)
