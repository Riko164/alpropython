def hitungipk(ip,sks):
    return ip/sks
ips=0
sks=0
ip=float(input("Masukkan IPS semester 1: "))
sk=float(input("Masukkan SKS semseter 1: "))
sks+=sk
ips+=(ip*sk)
print("IPK: ",hitungipk(ips,sks))
print("="*30)
ip=float(input("Masukkan IPS semester 2: "))
sk=float(input("Masukkan SKS semseter 2: "))
sks+=sk
ips+=(ip*sk)
print("IPK: %.2f"%hitungipk(ips,sks))
print("="*30)
ip=float(input("Masukkan IPS semester 3: "))
sk=float(input("Masukkan SKS semseter 3: "))
sks+=sk
ips+=(ip*sk)
print("IPK: %.2f"%hitungipk(ips,sks))
print("="*30)
ip=float(input("Masukkan IPS semester 4: "))
sk=float(input("Masukkan SKS semseter 4: "))
sks+=sk
ips+=(ip*sk)
print("IPK: %.2f"%hitungipk(ips,sks))
print("="*30)
