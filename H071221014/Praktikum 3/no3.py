from math import floor
print("\n====================================")
print("    PROGRAM MENGHITUNG KEMBALIAN    ")
print("====================================")

harga_barang = int(input(''))
nilai_uang = int(input(''))
kembalian = int(nilai_uang - harga_barang) #kembalian

seratusribu = limapuluh = duapuluh = sepuluhribu = limaribu = duaribu = seribu = 0


if kembalian<=0 :
    print("Tidak ada kembalian")
else :
    while kembalian>=100000 :
        d = floor(kembalian/100000) #Variabel d untuk menentukan berapa lembar kembaliannya
        seratusribu += d
        kembalian = kembalian%100000 #ini untuk menentukan apakah ada kembalian lebih dari 100rb dan jika ada akan dimasukkan ke variabel d (lembar uang)
    while kembalian>=50000 :
        d = floor(kembalian/50000)
        limapuluh += d
        kembalian = kembalian%50000
    while kembalian>=20000 :
        d = floor(kembalian/20000)
        duapuluh += d
        kembalian = kembalian%20000
    while kembalian>=10000 :
        d = floor(kembalian/10000)
        sepuluhribu += d
        kembalian = kembalian%10000
    while kembalian>=5000 :
        d = floor(kembalian/5000)
        limaribu += d
        kembalian = kembalian%5000
    while kembalian>=2000 :
        d = floor(kembalian/2000)
        duaribu += d
        kembalian = kembalian%2000
    while kembalian>=1000 :
        d = floor(kembalian/1000)
        seribu += d
        kembalian = kembalian%1000
        
    print(seratusribu, "uang Rp.100.000")
    print(limapuluh, "uang Rp.50.000")
    print(duapuluh, "uang Rp.20.000")
    print(sepuluhribu, "uang Rp.10.000")
    print(limaribu, "uang Rp.5.000")
    print(duaribu, "uang Rp.2.000")
    print(seribu, "uang Rp.1.000")
