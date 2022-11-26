class Elektronik:
    def __init__(self, merk) -> None:
        self._harga = 0
        self.merk = merk

    def setHarga(self, harga):
        self._harga = harga
    
    def getHarga(self):
        return self._harga

    def nyalakan(self):
        print(f"{self.merk} Menyala")

class Handphone(Elektronik):
    def __init__(self, merk, harga):
        super().__init__(merk)
        self.harga = harga
        self.baterai = 5

    def charge(self):
        self.baterai = 100

    def layar(self):
        print(f"{self.merk} Layarnya Kecil")

    def nyalakan(self):
        print(f'Handphone {self.merk} Menyala')


class Laptop(Elektronik):
    def __init__(self, merk, harga):
        super().__init__(merk)
        self.harga = harga
        self.baterai = 10

    def layar(self):
        print(f"{self.merk} Layarnya Besar")
    

HP = Handphone("Samsung", 5000)
laptop = Laptop("Asus", 20000)

HP.nyalakan()
HP.layar()
laptop.layar()