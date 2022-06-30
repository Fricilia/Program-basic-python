
# coding: utf-8

# In[1]:

# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")


# In[2]:

# Python program to domanstrate
# Adding Elements to a Array

# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])

print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print ("Array before insertion : ", end =" ")
for i in range (0, 3 ):
    print (b[i], end =" ")
print()

# adding an element using append()
b.append(4.4)

print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()


# In[3]:

# Python program to demonstrate 
# accessing of element from list

# importing array module
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print ("Access element is: ", a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing elemen of array
print("Access element is: ", b[1])

# accessing element of array
print("Access element is: ", b[2])


# In[4]:

# Python program to demonstrate
# Removal of elements in a array

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 5):
    print (arr[i], end =" ")
    
print ("\r")

# using pop() to remove element at 2nd position
print ("The popped element is : ", end =" ")
print (arr.pop(2))

# printing array after popping
print ("The array after popping is : ", end =" ")
for i in range (0, 4):
    print (arr[i], end =" ")
    
print("\r")

# using remove() to remove 1st occurence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is: ", end =" ")
for i in range (0, 3):
    print (arr[i], end =" ")


# In[7]:

# Python program to demonstrate
# silicing o elements in a Array

# importing array module
import array as arr

# creating a list
import array as arr

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end =" ")
    
# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "elemennt till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)


# In[9]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]

print(type(foo))
print(type(bar))
print(type(baz))


# In[10]:

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]

print(foo[0])
print(foo[1])
print(foo[2])
print(foo[3])
print(foo[4])
print(foo[5])


# In[11]:

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo)

foo[0] = 'Belajar'
foo[3] = False
print(foo)


# In[12]:

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])


# In[14]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))
foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))


# In[15]:

foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)

print(foo[0])
print(foo[1])
print(foo[2])
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:1])


# In[19]:

foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
foo[0] = 'Belajar'
print(foo)


# In[20]:

foo = {"Belajar", "Python", "di", "Duniailkom"}
bar = {100, 200, 300, 400}
baz = {"Python", 200, 6.99, True}

print(foo)
print(bar)
print(baz)


# In[22]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))

foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))

foo = {"Belajar", "Python", "di", "Duniailkom"}
print(type(foo))


# In[1]:

foo = { 1: "Belajar", 2: "Python", 3: "di Duniailkom" }
bar = { "mengapa": "Belajar", "apa": "Python", "dimana": "di Duniailkom" }
baz = { 1: "Belajar", "apa": "Python", "dimana": "di Duniailkom" }

print(type(foo))
print(type(bar))
print(type(baz))

print(foo)
print(bar)
print(baz)


# In[ ]:




# In[4]:

foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom" ,
        "hasil": "Yakin bisa!" }

print(foo["website"])


# In[6]:

foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }

foo["kegiatan"] = "Belajar Bahasa Pemrograman"
print(foo)


# In[7]:

foo = { "kegiatan" : "Belajar Python",
        "website" : "Duniailkom",
        "hasil" : "Yakin bisa!" }

foo["target"] = 2020
print(foo)


# In[8]:

foo = { "kegiatan" : "Belajar Python",
        "website" : "Duniailkom",
        "hasil" : "Yakin bisa!" }

del foo["kegiatan"]
print(foo)


# In[9]:

foo = dict ( kegiatan = "Belajar Python",
             website = "Duniailkom",
             hasil = "Yakin bisa!" )

print(foo)


# In[ ]:



