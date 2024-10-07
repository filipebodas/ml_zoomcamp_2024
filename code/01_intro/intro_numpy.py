import numpy as np

# Create arrays
np.zeros(10)
np.ones(10) 
np.full(10, 2.5) # array size 10

a = np.array([1, 2, 3, 5, 7, 12])
a[2] # access number 3 --> position 2

# replace 3 by 10
a[2] = 10
a

np.arange(10) 
np.arange(3, 10) # array that starts with 3 incluse, and ends in 10 exclusive

np.linspace(0,1, 11) # creates an array size 11, where the first element is 0 and the last is 1

# Create multi-dimensional arrays
np.zeros((5,2)) # 5 rows and 2 columns

n = np.array([
        [1,2,3],
        [3,5,6],
        [3,0,2]
        ])

n[0,1] # access element 2 in the first row
n[0] # access entire row
n[:, 1] # access a column we need the ":" and ","

# Random arrays
np.random.seed(3) #to fix the results
np.random.rand(5, 2)

np.random.randn(5, 2) # random uniform distribution

np.random.randint(low = 0, high = 100, size = (5,2))

a 
a + 2
a * 3
b = (10 + (a*2)) ** 2

a + b # add arrays

a > b # compare arrays
a >= 2

a < b # all elements are true...
a[a < b] #... therefore it returns all elements in array a that are true

a.max()
a.min()
a.mean()
a.std()