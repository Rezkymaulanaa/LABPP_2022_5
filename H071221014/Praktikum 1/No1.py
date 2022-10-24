print('\nPROGRAM MENGHITUNG KAPAL')

h=float(input('\nMasukkan Tinggi Menara : '))
a=int(input('Sudut elevasi pengamat pada ujung belakang kapal :'))
b=int(input('Sudut elevasi pengamat pada ujung depan kapal : '))


import math
rad_a= 3.1415926535898/180*a
tan_a= (math.tan(rad_a))

rad_b= 3.1415926535898/180*b
tan_b= (math.tan(rad_b))

ac= tan_a*h
bc= tan_b*h

# ab= math.sqrt(math.pow(ac-bc,2))
ab = (ac-bc)**2
AB = ab**(0.5)
#AB adalah panjang kapal
print('Panjang kapal adalah : ', round(AB,1), 'm')
