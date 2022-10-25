filename = input() + ".txt"
n = int(input())

f = open(filename, "w+")

try:
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    f.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(n):
        nama = input().replace(" ","_")
        if len(nama) > 20:
            raise TypeError
        nim = input()
        angkatan = input()
    
        f.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " | " + angkatan + " "*5 + "|" + "\n")
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    
    print("Berhasil")
except:
    print("Gagal")
    
f.close()