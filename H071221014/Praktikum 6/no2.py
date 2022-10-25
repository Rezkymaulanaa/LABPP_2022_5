try:
    a = input("Masukkan nama file : ") + '.txt'
    b = input("Masukkan nama file salinan : ") + '.txt'
    cek_len = 0
    with open(a, 'r') as origin :
        for x in origin :
            if len(x) > cek_len:
                cek_len = len(x)

    with open(a, 'r') as origin:
        r = 1
        s = len(origin.readlines())

    with open(a, 'r') as origin:
        copy = open(b, 'w')
        for i in origin:
            if r<s :
                new_text = f'{i.rstrip():>{cek_len}}\n'
            else : 
                new_text = f'{i.rstrip():>{cek_len}}'
            copy.write(new_text)
            r+=1
        copy.close()
    print('\nBerhasil')

except:
    print('\nGagal')