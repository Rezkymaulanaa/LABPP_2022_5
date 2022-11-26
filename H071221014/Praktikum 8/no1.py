class Person: 
    def __init__(self, nama, umur, gender):
        self.name = nama
        self.age = umur
        self.isMale = gender

    def setName(self, nama):
        self.name = nama
    def getName(self):
        print(f"Nama : {self.name}")

    def setAge(self, umur):
        self.age = umur
    def getAge(self):
        print(f"Umur : {self.age}")

    def setGender(self, gender):
        self.isMale = gender
    def getGender(self):
        if self.isMale == True:
            print('Gender : Laki-laki')
        else:
            print('Gender : Perempuan')
    
alif = Person('Alif', 19, True)
alif.getName()
alif.getAge()
alif.getGender()
