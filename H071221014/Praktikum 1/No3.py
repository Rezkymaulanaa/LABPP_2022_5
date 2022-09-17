print('\nPROGRAM MENGHITUNG GAJI')

nama_seller= input('\nNama Seller : ')
gaji_pokok= float(input('Masukkan Gaji Pokok : '))
total_penjualan= float(input('Masukkan Total Penjualan : '))

total_penghasilan= (15/100)*total_penjualan
total_gaji= gaji_pokok + total_penghasilan

print('\nTOTAL GAJI YANG DITERIMA ADALAH : $', round(total_gaji,2))
