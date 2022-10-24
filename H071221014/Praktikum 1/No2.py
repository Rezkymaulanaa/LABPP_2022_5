print('\nPROGRAM KONVERSI DETIK KE JAM')
detik_raw=int(input('\nMasukkan jumlah detik yang ingin di konversi : '))

jam= detik_raw //3600
sisa_detik= detik_raw %3600
menit= sisa_detik // 60
detik= sisa_detik % 60



print("%02d:%02d:%02d" % (jam,menit,detik))