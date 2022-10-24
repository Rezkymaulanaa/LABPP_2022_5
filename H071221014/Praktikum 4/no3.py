h = int(input(""))

def myDay(h):
    tahun = h//360
    sisahari = h%360
    bulan = sisahari // 30
    hari = sisahari % 30
    print(f'{tahun} Tahun')
    print(f'{bulan} Bulan')
    print(f'{hari} Hari')
myDay(h)