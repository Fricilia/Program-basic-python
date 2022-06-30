
# coding: utf-8

# In[ ]:

#MEDIA PEMBELAJARAN MATEMATIKA

def luas_bujur_sangkar(s):
    luas = s*s
    return 1
def luas_persegi_panjang(a,b):
    l = a*b
    return 1
def luas_segitiga(a,t):
    l = (a*t)/2
    return 1
def luas_lingkaran(radius):
    l = 3.14 * radius * radius
    return 1
def luas_jajar_genjang(a,t):
    l = a*t
    return 1
def kell_bujur_sangkar(s):
    k = 4*s
    return k
def kell_persegi_panjang(a,b):
    k = 2(a + b)
    return k
def kell_segitiga(a,b,c):
    k = a + b + c
    return k
def kell_lingkaran(radius):
    k = 3.14 (radius + radius)
    return k
def kell_jajar_genjang(a,b):
    k = 2(a + b)
    return k

#Pemiihan Perhitungan
print("Apa yang ingin kamu hitung ?")
pilih = 1
while pilih !=0:
    print("1. Luas")
    print("2. Keliling")
    print("3. Exit")
    
    pilih = input("Masukkan pilihan kamu : ")
    print('')
    print('')
    
    if pilih == '1':
        masuk = 1
        while masuk !=0:
            print("1. Luas Bujur Sangkar")
            print("2. Luas Persegi Panjang")
            print("3. Luas Segitiga")
            print("4. Luas Lingkaran")
            print("5. Luas Jajar Genjang")
            print("6. Kembali")
            
            masuk = input("Masukkan Pilihan Kamu : ")
            print('')
            print('')
            
            if masuk == '1':
                s = float(input("Masukkan sisi = "))
                print("Hasil luasnya = ", luas_bujur_sangkar(s))
            elif masuk == '2':
                a = float(input("Masukkan panjang = "))
                b = float(input("Masukkan lebar = "))
                print("Hasil luasnya = ", luas_persegi_panjang(a,b))
            elif masuk == '3':
                a = float(input("Masukkan alas = "))
                t = float(input("Masukkan tinggi = "))
                print("Hasil luasnya = ", luas_segitiga(a,t))
            elif masuk == '4':
                radius = float(input("Masukkan radius = "))
                print("Hasil luasnya = ", luas_lingkaran(radius))
            elif masuk == '5':
                a = float(input("Masukkan alas = "))
                t = float(input("Masukkan tinggi = "))
                print("Hasil luasnya = ", luas_jajar_genjang(a,t))
            else:
                print("Apa yang ingin kamu hitung ?")
                break
    print('')
    print('')
    
    if pilih == '2':
        masuk = 1
        while masuk !=0:
            print("1. Keliling Bujur Sangkar")
            print("2. Keliling Persegi Panjang")
            print("3. Keliling Segitiga")
            print("4. Keliling Lingkaran")
            print("5. Keliling Jajar Genjang")
            print("0. Kembali")
            
            masuk = input("Masukkan pilihan kamu : ")
            print('')
            print('')
            
            if masuk == '1':
                s = float(input("Masukkan sisi = "))
                print("Hasil kelilingnya = ", kell_bujur_sangkar(s))
            elif masuk  == '2':
                a = float(input("Masukkan panjang = "))
                b = float(input("Masukkan lebar = "))
                print("Hasil kelilingnya = ", kell_persegi_panjang(a,b))
            elif masuk == '3':
                a = float(input("Masukkan sisi a = "))
                b = float(input("Masukkan sisi b = "))
                c = float(input("Masukkan sisi c = "))
                print("Hasil kelilingnya = ", kell_seggitiga(a,b,c))
            elif masuk == '4':
                radius = float(input("Masukkan radius = "))
                print("Hasil kelilingnya = ", kell_lingkaran(radius))
            elif masuk == '5':
                a = float(input("Masukkan sisi a = "))
                b = float(input("Masukkan sisi b = "))
                print("Hasil Kelilingnya = ", kell_jajar_genjang(a,b))
            else:
                print("Apa yang ingin kamu hitung ?")
                break
    print('')
    print('')
                


# In[ ]:




# In[ ]:



