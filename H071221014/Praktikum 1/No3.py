print('\nPROGRAM MENGHITUNG GAJI')

nama_seller= input('\nNama Seller : ')
gaji_pokok= float(input('Masukkan Gaji Pokok : '))
total_penjualan= float(input('Masukkan Total Penjualan : '))

total_penghasilan= (15/100)*total_penjualan
total_gaji= gaji_pokok + total_penghasilan

print('\nTOTAL = $', round(total_gaji,2))
