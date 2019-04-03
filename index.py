# working with NumPy
import  numpy as np
# Creating Arrays

array_one = np.array([1,2,3,4])
print(array_one)

numbers = [9,8,7,6]
arrays_two = np.array(numbers)
print(arrays_two)

array_of_zeros = np.zeros((3,4),dtype=np.int16)
print(array_of_zeros)

array_of_ones = np.ones((3,4),dtype=np.int16)
print(array_of_ones)

array_eye = np.eye(4,dtype=np.int16)   # idenity matrix
print(array_eye)

array_of_evens = np.arange(2,20,2)
print(array_of_evens)

array_2d = np.array([(2,4,6),(3,5,7)])
print(array_2d)

array_nd = np.arange(6).reshape(3,2)
print(array_nd)

array_ones = np.ones_like(array_nd)   # make an array of one's, the same size as this array
print(array_ones)

# Printing Arrays

# Basic Array Operations

# Universal Functions

salaries = np.genfromtxt('salary.csv',delimiter=',')
salaries
print(salaries)

salaries.shape
mean =  np.mean(salaries)
median = np.median(salaries)
sd = np.std(salaries)
variance = np.var(salaries)

print('Mean = %i' %mean)


# Indexing and slicing Arrays

# Iterating Over Arrays

# Reshaping Arrays

# Splitting Arrays Horizontally and Vertically

# Image manipulation

# Shallow Copies Using view

# Deep Copies Using copy
