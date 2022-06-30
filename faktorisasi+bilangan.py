
# coding: utf-8

# In[2]:

#progam menentukan faktorisasi bilangan
#masih belum bisa dibalik dari bilangan besar ke kecil :)

def print_faktor(x):
    """Fungsi menerima input bilangan dan mencetak faktornya"""
    print("Faktor dari", x, "adalah:")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
num = int(input("Masukkan bilangan: "))
print_faktor(num)


# In[ ]:



