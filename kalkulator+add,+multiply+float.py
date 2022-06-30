
# coding: utf-8

# In[7]:

#PROGRAM MENJUMLAH DAN MENGALIKAN DUA BUAH BILANGAN
def add(x,y): # funsi penjumlahan
    return x + y
def multiply(x, y): # fungsi perkalian
    return x * y
#menu operasi
print ("pilih operasi")
print ("1.jumlah")
print ("2.kali")
choise = input ("masukkan pilihan(1/2): ") #meminta input dari user
num1 = float(input("masukkan bilangan pertama: "))
num2 = float(input("masukkan bilangan kedua: "))
if choise == '1':
    print (num1,"+",num2,"=", add(num1,num2))
elif choise == '2':
    print (num1,"*",num2,"=", multiply(num1,num2))
else:
    print ("input salah")


# In[6]:

2


# In[ ]:



