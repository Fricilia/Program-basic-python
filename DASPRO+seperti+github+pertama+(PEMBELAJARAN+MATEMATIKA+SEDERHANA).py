
# coding: utf-8

# In[ ]:

#Program Kalkulator Sederhana
#Job Sheet 4 Dasar Pemrograman

def luas_bujur_sangkar(sisi) :
    luas = sisi * sisi
    return luas
def keliling_bujur_sangkar(sisi) :
    keliling = 4 * sisi
    return keliling
def luas_persegi_panjang(panjang,lebar) :
    luas = panjang * lebar
    return luas
def keliling_persegi_panjang(panjang,lebar):
    keliling = 2 * (panjang + lebar) 
    return keliling
def luas_segitiga(alas,tingi) :
    luas = 0.5 * alas * tinggi
    return luas
def keliling_segitiga(a, b, c) :
    keliling = a + b + c
    return keliling
def luas_jajar_genjang(alas,tinggi) :
    luas = alas * tinggi
    return luas
def keliling_jajar_genjang(alas,miring) :
    keliling = 2 * (alas + miring)
    return keliling
def luas_lingkaran(radius) :
    luas = 3.14 * radius * radius
    return luas
def keliling_lingkaran(radius) :
    keliling = 2 * 3.14 * radius
    return keliling

pilihan = 1
while pilihan !=0:
    print('PEMBELAJARAN MATEMATIKA SEDERHANA')
    print('SILAHKAN PILIH OPSI : ')
    print('1. Luas bujur sangkar')
    print('2. Keliling bujur sangkar')
    print('3. Luas persegi panjang')
    print('4. Keliling persegi panjang')
    print('5. Luas segitiga')
    print('6. Keliling segitiga')
    print('7. Luas jajar genjang')
    print('8. Keliling jajar genjang')
    print('9. Luas lingkaran')
    print('10. Keliling lingkaran')
    print('0. exit')
    
    pilihan = int(input('masukkan nomor opsi :'))
    if pilihan ==1 :
        print('\n')
        print('Luas bujur sangkar')
        sisi = int(input('sisi :'))
        print('Luas bujur sangkar :%d\n' %luas_bujur_sangkar(sisi))
    elif pilihan ==2 :
        print('\n')
        print('Keliling bujur sangkar')
        sisi = int(input('sisi :'))
        print('Keliling bujur sangkar :%d\n' %keliling_bujur_sangkar(sisi))
    elif pilihan ==3 :
        print('\n')
        print('Luas persegi panjang')
        panjang = int(input('panjang: '))
        lebar = int(input('lebar :'))
        print('Luas persegi panjang :%d\n' %luas_persegi_panjang(panjang,lebar))
    elif pilihan ==4 :
        print('\n')
        print('Keliling persegi panjang')
        panjang = int(input('panjang :'))
        lebar = int(input('lebar :'))
        print('Keliling persegi panjang :%d\n' %keliling_persegi_panjang(panjang,lebar))
    elif pilihan ==5 :
        print('\n')
        print('Luas segitiga')
        alas = int(input('alas :'))
        tinggi = int(input('tinggi :'))
        print('Luas segitiga :%d\n' %luas_segitiga(alas,tinggi))
    elif pilihan ==6 :
        print('\n')
        print('Keliling segitiga :')
        a = int(input('a :'))
        b = int(input('b :'))
        c = int(input('c :'))
        print('Keliling segitiga :%d\n' %keliling_segitiga(a,b,c))
    elif pilihan ==7 :
        print('\n')
        print('Luas jajar genjang :')
        alas = int(input('alas :'))
        tinggi = int(input('tinggi :'))
        print('Luas jajar genjang :%d\n' %luas_jajar_genjang(alas,tinggi))
    elif pilihan ==8 :
        print('\n')
        print('Keliling jajar genjang :')
        alas = int(input('alas :'))
        miring = int(input('miring :'))
        print('Keliling jajar genjang :%d\n' %keliling_jajar_genjang(alas,miring))
    elif pilihan ==9 :
        print('\n')
        print('Luas lingkaran :')
        radius = int(input('radius :'))
        print('Luas lingkaran :%d\n' %luas_lingkaran(radius))
    if pilihan ==10 :
        print('\n')
        print('Keliling lingkaran :')
        radius = int(input('radius :'))
        print('Keliling lingkaran :%d\n' %keliling_lingkaran(radius))


# In[ ]:



