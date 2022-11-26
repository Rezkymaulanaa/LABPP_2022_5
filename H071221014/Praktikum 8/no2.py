class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang

    
    def setMassa(self, massa):
        self.massa = float(massa)
    
    def setLebar(self, lebar):
        self.lebar = float(lebar)
    
    def setPanjang(self, panjang):
        self.panjang = float(panjang)
    
    def setTinggi(self, tinggi):
        self.tinggi = float(tinggi)

    def getMassaJenis(self):
        return self.massa/(self.lebar*self.tinggi*self.panjang)

lebar = float(input("Lebar : "))
tinggi = float(input("Tinggi : "))
panjang = float(input("Panjang : "))
massa = float(input("Massa : "))

kubus = Kubus(lebar,tinggi,panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())
