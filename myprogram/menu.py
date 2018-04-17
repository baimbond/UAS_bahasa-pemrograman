def menu():
    print("=============================================")
    print("\n\t----Pilihan-----")
    print("\t1. Penilaian Mahasiswa")
    print("\t2. Pembayaran Mahasiswa")
    
    
    pilih = input("\n\tSilahkan pilih : ")
    if pilih == "1" :
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/n) ?")
    if tanya == "y":
        menu()
    elif tanya == "n":
        exit
    else:
        print("\n\tSalah Input !!")
