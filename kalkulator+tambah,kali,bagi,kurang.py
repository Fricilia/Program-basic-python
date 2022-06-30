
# coding: utf-8

# In[2]:

#KALKULATOR SEDERHANA
def add (x, y): # fungsi penjumlahan
    return x + y
def subtract (x, y): #fungsi pengurangan
    return x - y
def multiply (x,y): # fungsi perkalian
    return x * y
def divide (x, y): #fungsi pembagian
    return x / y
#menu operasi
print ("pilih operasi")
print ("1.jumlah")
print ("2.kurang")
print ("3.kali")
print ("4.bagi")
choise = input ("masukkan pilihan(1/2/3/4): ") #meminta input dari user
num1 = int(input("masukkan bilangan pertama: "))
num2 = int(input("masukkan bilangan kedua: "))
if choise == '1':
    print (num1,"+",num2,"=", add(num1,num2))
elif choise == '2':
    print (num1,"-",num2,"=", subtract(num1,num2))
elif choise == '3':
    print (num1,"*",num2,"=", multiply(num1,num2))
elif choise == '4':
    print (num1,"/",num2,"=", divide(num1,num2))
else:
    print ("input salah")


# In[ ]:



