
try:
    a = input('Masukkan nama file : ') + '.txt'
    fileasli = open(a,'r')

    b = input('Masukkan nama file salinan : ') + '.txt'
    with open(b,'w') as copy:
        for i in fileasli:
            if i[len(i)-1] == '\n' :
                spasi = " "*(18-len(i))
            else:
                spasi = " "*(17-len(i))
            copy.write(spasi + i)
    print('\nBerhasil')
except:
    print('\nGagal')

fileasli.close()
