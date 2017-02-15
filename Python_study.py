
# coding: utf-8

# # Python list study

# In[1]:

a = [66.25, 333, 333, 1, 1234.5]
a.count(333)
a.insert(2,-1)
a.index(333)
a.remove(333)
a.sort()
a.pop()
a.reverse()
del a[0]


# In[2]:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])


# In[3]:

squares = [x**2 for x in range(10)]
squares


# In[4]:

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


# # Set

# In[5]:

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
fruit
set(['orange', 'pear', 'apple', 'banana'])
'orange' in fruit                 # fast membership testing
True
'crabgrass' in fruit
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
a & b                              # letters in both a and b
set(['a', 'c'])
a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])


# In[6]:

a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[ ]:



