
# coding: utf-8

# In[1]:

#import the pandas Library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df)


# In[4]:

#import the pandas Library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby ('Team').groups)


# In[5]:

#import the pandas Library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby (['Team', 'Year']).groups)


# In[6]:

#import the pandas Library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')

for name,group in grouped:
    print (name)
    print(group)


# In[7]:

#import the pandas Library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print (grouped.get_group(2014))


# In[9]:

#import the pandas Library
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print (grouped['Points'].agg(np.mean))


# In[10]:

#import the pandas Library
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Team')
print (grouped['Points'].agg([np.sum, np.mean, np.std]))


# In[11]:

#import the pandas Library
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))


# In[12]:

#import the pandas Library
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'], 
   'Rank': [1, 2, 2, 3, 3,4 , 1, 1,2 , 4,1,2], 
   'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017], 
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby('Team').filter(lambda x: len(x) >= 3))


# In[14]:

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


# In[15]:

# List alfabet
alfabet = ['a', 'b', 'c', 'e', 'i', 'k', 'o', 'z']
# fungsi penyaringan huruf vocal
def filter_vocal(alfabet):
    vocal = ['a', 'i', 'u', 'e', 'o']
    if alfabet in vocal:
        return True
    else:
        return False

vocal_terfilter = filter(filter_vocal, alfabet)
print('Huruf vocal yang tersaring adalah: ')
for vocal in vocal_terfilter:
    print(vocal)


# In[18]:

# Python code to demonstrate working of
# heapyfy(), heappush() and heappop

#importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

#using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push element into heap
# pushes 4
heapq.heappush(li,4)

# printing modifed heap
print ("The modified heap after push is : ",end="")
print (list(li))

#using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


# In[19]:

# Python code to demonstrate working of
# heappushpop() and heapreolce()

# importing "heapq" to implement heap queue
import heapq

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))

# using heappushpop() to push and pop items simultaneously
# pops 3
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li2, 2))


# In[20]:

# Python code to demonstrate working of
# nlargest() and nsmallest()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest number
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 largest number
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))


# In[1]:

# Python program showing a use
# lambda function

# performing a adition of three number
x1 = (lambda x, y, z: (x + y) * z)(1, 2, 3)
print(x1)

#function using a lambda function
x2 = (lambda x, y, z: (x + y) if (z == 0) else (x * y))(1, 2, 3)
print(x2)


# In[2]:

# python code to illustrate cube of a number
# showing differencce between def() and lambda()
def cube(y):
    return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))


# In[3]:

# Python program performing
# operation using def
def fun(x, y, z):
    return x*y*z
a = 1
b = 2
c = 3

# logical jump
d = fun(a, b, c)
print(d)


# Python program performing
# operation using lambda

d = (lambda x, y, z: x*y+z)(1, 2, 3)
print(d)


# In[5]:

def func(x):
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    else:
        return "ten"
num = func(3)
print(num)

# Python program showing use
# of lambda function
num = (lambda x: "one" if x == 1 else ("two" if x == 2
                        else ("three" if x == 3 else "ten")))(3)
print(num)


# In[6]:

# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# In[8]:

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)


# In[ ]:

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce

