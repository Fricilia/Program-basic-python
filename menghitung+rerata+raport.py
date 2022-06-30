
# coding: utf-8

# In[1]:

#PROGRAM MENGHITUNG RATA RATA RAPOR SISWA
array = []
total = 0

n = int(input("Masukkan Banyaknya Mata Pelajaran: "))
for x in range(n):
    nilai = float(input("Masukkan Nilai ke-{} : ".format(x+1)))
    array.append(nilai)
    
print("\nNilai total rapor adalah : {}".format(sum(array)))
print("Nilai rata-rata rapor adalah : {}".format(sum(array)/n))


# In[4]:

#PROGRAM MENGHITUNG RATA RATA RAPOR SISWA
array = []
total = 0

n = int(input("Masukkan Banyaknya Mata Pelajaran: "))
for x in range(n):
    nilai = float(input("Masukkan Nilai ke-{} : ".format(x+1)))
    array.append(nilai)
    
print("\nNilai total rapor adalah : {}".format(sum(array)))
print("Nilai rata-rata rapor adalah : {}".format(sum(array)/n))


# In[ ]:



