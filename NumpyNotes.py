"""

Numpy is numerical python
its a libary for number crunching

you can store data in multi dimensional arrays

why use numpy over lists?
lists are slow, numpy is fast.

why are lists slow
numpy uses fixed types, this makes it fast

computers see numbers as binary
lists use a built in int type for python
    it consists of object val,object type, ref count, and size of int value
    This requris alot more space than numpy
because numpy uses less bytes of memory to represent numbers, pc can read it faster
with numpy, we dont have to do type checking when iterating through objects 

numpy also faster than lists because numpy uses contig memory
with lists, list would be scattered around in computer memory, not contig
    if you have 8 item list, the list has pointers to elements scattered around in memory
    this is not fat
numpy array however uses contig memory, all 8 blocks would be next to eachother

computers have SIMD vector processing -> single instruct multiple data
    we can use SIMD to perform computations on all the vals in one go 
    when data is contig placed

we can also use our cached more effectively because everything is next to eachtoehr


HOW ARE LISTS DIFF FROM NUMPY
    big diff, within numpy we can do lots more on numpy arrays
    than on lists

    in numpy we can do single value multiplication
    like 1 * 1, 3 * 2, 5 * 3
    
    a = np.array([1,3,5])
    b = np.array([1,2,3])
    # result
    a*b = np.array([1,6,15])
----------------------------------------------------------

APPLICATIONS OF NUMPY

matlab replacement, we can do lots of math
scipy lab has even more math functions than numpy
useful for plotting
backend for pandas, connect 4, digital photography 
    such as storing images in numpy
useful for machine learning



"""

import numpy as np

#initialize array
#we pass in a list to array function
a = np.array([1,2,3],dtype='int32') #or int16
#int32 is 4 bytes, int16 is 2 bytes
# print(a)

#array of floats
b = np.array([[9.0,8.0,7.0],[6.0,1.3,5.4]])
# print(b)

#get dimensions of array
a.ndim # 1
b.ndim # 2

#get shape
a.shape # (3,) a is a vector, it only has 1 dimension
b.shape # (2,3) 2 rows, 3 cols

#get type
a.dtype
b.dtype

#get size
a.itemsize # 4 bytes

#get total size (# of elements * element size)
a.size * a.itemsize # 12
#Alternative
#a.bytes

b.itemsize #8 bytes because b contains floats



#ACCESSING/CHANGING SPECIFIC ROWS,COLUMSN etc
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)
#prove its 2 x 7 by using shape
a.shape # (2,7)

#to get a specific element
#use [r,c]
a[1,5] #13 because rows are 0 based indexing
#can also use negative notation
a[1,-2] # 13 because its 2nd from last

#GET SPECIFIC ROW
a[0,:] # gives eveything in row 0
#GET SPECIFIC COL
a[:,2] # 


#GETTING FANCY
#[startindex:endindex:stepsize]
a[0, 1:6:2] #start at first row, start at 2, end at 6, step size 2

#CHANGE A VALUE
a[1,5]=20 #changes element at row 1, col 5 to 20 (13->20)
# print(a)

#CHANGE all vals in column
a[:,2] = 5
# print(a)
#make it 2 different numbers, specify the same shape that you subsequenced
a[:,2] = [1,2]


#3D example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)

#get specific element from 3d ex
#work from outside inward
b[0,1,1] #4
#alternate
b[:,1,:]

#replace in 3D
#make reaplcement the same dimension as what you want to replace
# b[:,1,:1] = [[9,9,9],[8,8],[1,2]]


"""
INITIALIZTING DIFFERENT TYPES OF ARRAYS
"""

#all zeroes matrix
a = np.zeros(5) #gives a vector of size 5 with all 0's
b = np.zeros([2,3])

# all 1's matrix
np.ones((4,2,2))
#Can also specify data type
np.ones((3,2,2),dtype='int32')

#a regualar array with w.e nums you want
#specify shape and then values ((shape),values)
np.full((2,2),99)
np.full((2,2),99, dtype='float32')

#any other number (full_like)
#take shape from existing array shape and use to build same shape 
np.full_like(a.shape,4)

#Random decimal numbers between 0 and 1
np.random.rand(4,2)

#Random deciman nums from existing array shape
np.random.random_sample(a.shape)

#random integer vals
#if you dont specify number, it will start at 0
#if you dont specify a shape
np.random.randint(7, size=(3,3))
np.random.randint(-4,8, size=(3,3))

#Identity matrix
np.identity(3)


#repeat array a few times
arr= np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)


#EXERCISE
# https://youtu.be/QUT1VHiLmmI?t=1921
a = np.ones([5,5])
#make array of all zeroes
z = np.zeros((3,3))
#set middle element to 9 in zeroes array
z[1,1]=9
#replace first row,first col to 3rd row,3rd col of A with Z
a[1:4,1:4] = z
print(a)


#something to becareful with
#in setting b to a, we not making a copy of a's contents
#we are only pointing b to the same thing a is pointing to
#so when we change somethign in b, it changes it for a too
a = np.array([1,2,3])
b = a
b[0] = 100
print(a)

#to overcome the above
# we use a.copy
#this makes a copy of a's contents
a = np.array([1,2,3])
b = a.copy
b[0] = 100
print(b)



#MATH CAPABILITIES OF NUMPY
#element-wise arithmetic

a + 2 #adds 2 to each element
a - 2 #subtracts 2 from each element
a * 2 #multiplies each element by 2
a / 2 #divides everything by 2
a += 2 #2 plus everything
a ** 2 = # everything in a to second power
np.sin(a) #takes the sin of all the values
np.cos(a) #takes cosine of all values


b = np.array([1,0,1,0])
a + b 