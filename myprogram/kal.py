def tambah () :
    print('\t1. Penjumlahan')
    a = int(input('\tMasukkan nilai x = '))
    b = int(input('\tMasukkan nilai y = '))
    c = a+b
    print ('\tx + y = ',c)
    tanya()
def kurang () :
    print ('\t2. Pengurangan')
    a = int(input('\tMasukkan nilai x = '))
    b = int(input('\tMasukkan nilai y = '))
    c = a-b
    print ('\tx - y = ',c)
    tanya()
def kali () :
    print ('\t3. Perkalian')
    a = int(input('\tMasukkan nilai x = '))
    b = int(input('\tMasukkan nilai y = '))
    c = a*b
    print ('\tx * y = ',c)
    tanya()
def bagi () :
    print ('\t4. Pembagian')
    a = int(input('\tMasukkan nilai x = '))
    b = int(input('\tMasukkan nilai y = '))
    c = a/b
    print ('\tx / y = ',c)
    tanya()
def tanya() :
    tanya = input('Kembali Ke Menu kalkulator(Y/T)')
    if tanya=='Y' or tanya=='y':
        menu()
    elif tanya=='T' or tanya=='t':
        exit()
    else:
        print('Maaf Salah input')
        
def menu () :
    print ('\t_______________________________________________')
    print ('\n\t        Program Kalkulator Baimbond')
    print ('\t_______________________________________________')
    print ('\t1.penjumlahan')
    print ('\t2.Pengurangan')
    print ('\t3.Pembagian')
    print ('\t4.Perkalian')
    print ('\t______________________________________________')
    print ('\tSilahkan Pilih 1-4')
    print (' ')
    pil = input('\tMasukan Pilihan:')
    if pil=='1':
       tambah()
    elif pil=='2':
        kurang()
    elif pil=='3':
        kali()
    elif pil=='4':
        bagi()
    else:
        print('\n\tMaaf, input yang anda masukan salah,')
        print('\tCoba anda ulangi lagi yaa........\n')
menu()
tanya()
