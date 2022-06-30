
# coding: utf-8

# In[ ]:

nama = []
alamat = []
telepon = []

def harga():
    print("1. kertas \n2. plastik \n3. logam")
    jenis_sampah_anda = int(input("Apa jenis sampah anda? "))
    berat_sampah = float(input("Berapa kilo sampah anda? "))
    if pilihan == 1:
        sampah_kertas = berat_sampah * 2000
        print()
        print("Harga Sampah: ",sampah_kertas)
        print()
    elif pilihan == 2 :
        sampah_plastik = berat_sampah * 5000
        print()
        print("Harga sampah : ",sampah_plastik)
        print()
    else:
        sampah_logam = berat_sampah * 8000
        print()
        print("Harga sampah: ",sampah_logam)
        print()

print("================================================")
print("=\tUTS Algoritma & Pemrograman            =")               
print("=\tNama : Fricilia Yessi Eka Putri        =")           
print("=\tNIM  : 33420409                        =")                           
print("=\tKelas: IK1E                            =")
print("================================================\n")
print("\tLayanan Bank Sampah se Kecamatan Boja\n")
print("Silahkan login sebagai")

pilihan = 1
while pilihan != 0 :
    print ("1. Admin.")
    print ("2. Nasabah.")
    print ("0. exit.")
    
    pilihan = int(input("Masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1 :
        username = str(input("Masukkan username anda : "))
        import getpass
        password = str(input("Masukkan paswword anda : "))
        if(username=='Fricilia' and password=='33420409') :
            print("======================================")
            print("\tSELAMAT DATANG")
            print("======================================")
            print ("\nAnda telah login silahkan pilih akses di bawah ini")
            print("1. Tampilkan data")
            print("2. Hapus data")
            
            pilihan = int(input("masukan pilihan anda : "))
            print('')
            print('')
            if pilihan == 1 :
                penentu = True
                for i in range (len(telepon)) :
                    if penentu :
                        print ("nama\talamat\ttelepon")
                    print (nama[i]['nama'],'\t',alamat[i]['alamat'],'\t',telepon[i]['nomor telepon'])
                    penentu = False
            elif pilihan == 2 :
                masnama = input("Masukan nama : ")
                for i in range (len(nama)) :
                    if masnama == nama[i]['nama'] :
                        print (i)
                        del nama[i]
                        del alamat[i]
                        del telepon[i]
                        break
            else:
                print ("Nama atau password anda salah")
        
    elif pilihan == 2 :
        print("Silahkan lengkapi data untuk menjadi nasabah kami : ")
        masnama = input("Masukkan nama : ")
        nama.append({'nama' : masnama})
        masmat = input("Masukkan alamat : ")
        alamat.append({'alamat' : masmat})
        masnotelp = input("Masukkan nomor telepon : ")
        telepon.append({'nomor telepon' : masnotelp})
        print("\nAnda telah terdaftar sebagai nasabah kami, silahkan pilih opsi di bawah ini : \n")
        print("1. Harga Sampah /KG")
        print("2. Ingin Stor ")
        print("0. exit")
        print()
        pilihan = int(input("masukan pilihan anda : "))
        print('')
        print('')
        if pilihan == 1 :
            print("1. Kertas  = 2000/kg")
            print("2. Plastik = 5000/kg")
            print("3. Logam   = 8000/kg")
        elif pilihan == 2:
            harga() 


# In[ ]:



