
# coding: utf-8

# In[1]:

def segitiga():
    print("luas segitiga")
    print("================")
    s = 1/2
    a = float(input("masukkan alas : "))
    t = float(input("masukkan tinggi : "))
    luas = s * a * t
    print("luas segitiga = ", luas,"cm2")

segitiga()


# In[2]:

def luas_persegi_panjang(p, l):
    luas = p * l
    return luas

p = int(input("masukkan panjang : "))
l = int(input("masukkan lebar : "))
print("luas persegi panjang : ", luas_persegi_panjang(p, l))


# In[4]:

def luas_persegi_panjang(p, l):
    luas = p * l
    return luas
print "luas persegi panjang : %d" %luas_persegi_panjang(4, 2)


# In[5]:

def luas_persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    print(luas)
    
luas_persegi_panjang(4, 8)


# In[ ]:



