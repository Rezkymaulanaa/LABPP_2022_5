a = int(input(""))
b = int(input(""))
def getFPB(a, b):
    #saat b sama dengan nol maka return nilai a
    if (b == 0):
        return a
    #rekurens : saat b belum mencapai 0, maka terjadi rekursi
    else:
        return getFPB(b, a % b)

print(f"FPB ({a}, {b}) = {getFPB(a, b)}")
getFPB(a, b)