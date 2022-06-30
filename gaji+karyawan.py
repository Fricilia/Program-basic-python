
# coding: utf-8

# In[3]:

class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Fricilia ", 10000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Yessi", 1500000)
# Membuat objek pertama dari kelas Karyawan
karyawan3 = Karyawan("Eka ", 10000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)


# In[ ]:



