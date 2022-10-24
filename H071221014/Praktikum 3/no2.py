n = int(input(''))
angka1 = 0
angka2 = 1

for i in range(n):
    print(angka1,end=' ')
    angka_selanjutnya = angka1 + angka2
    angka1 = angka2
    angka2 = angka_selanjutnya