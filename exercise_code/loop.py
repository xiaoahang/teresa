outer_vals = [1, 2, 3]
inner_vals = ['A', 'B', 'C']

# nested loops
# inner loop runs to completion for each iteration of outer loop
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
# inner loop generates a single row of the table
# outer loop causes  multiple rows to be printed
for i in range(1, 7):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

# nested loops have many uses, e.g: sorting values into order
# Bubble sort
# # methods moves along the list, comparing adjacent values
# # swaps adjacent values if they are out of order
# # likened to moving a small window ( or 'bubble') along list
# # # compares values in window, and swao if needed

values = [4, 3, 6, 5, 2, 1]
N = len(values)
# range N-1 because , otherwise, accessing value at at position at i+ 1 will cause an index-out-of-bounds error
# here is ONE-TIME bubble, to get the max to the end of the array
for i in range(N - 1):
    if values[i] > values[i + 1]:
        tmp = values[i]
        values[i] = values[i + 1]
        values[i + 1] = tmp

for j in range(N):
    for i in range(N - 1):
        if values[i] > values[i + 1]:
            tmp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = tmp
# once N-1 items correctly in place, so also must be the final one
# after j runs of inner loop, j final items correct, so the elements behind j th items are correctly in place
for j in range(N - 1):
    for i in range(N - 1 - j):
        if values[i] > values[i + 1]:
            tmp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = tmp

# pylab Numberic Arrays
# pylab provides a special data type of numeric arrays
# todo read the source code of pylab & numpy
# for efficient storages of numbric data
# esp. large matrics
# memory efficient, fast matrix operations
#
# use zeros() function to create array of specified size
from pylab import *

zeros(5)
arange(0, 2, 0.3)

# 2D array with dimensions (3,5)
zeros((3, 5))
data = zeros((3, 5))
# these array have a shape attribute
data.shape

# use for loop to address the elements of a 2D array
values = zeros((3, 5))
val = 0
for row in range(3):
    for col in range(5):
        val += 0.1
        values[row][col] = val

print(values)

# use shape attributes to access dimensions if array
val = 0
(d1, d2) = values.shape
for row in range(d1):
    for col in range(d2):
        val += 0.1
        values[row][col] = val
#
#
# images are often represented as 2D arrays
# each array element represents the brightness or color of a puxel
# in a black/white image, each element is a number between 0.0 and 1.0, giving the itensity (brightness) of the pixel on a greyscale
# for each color image , each element might be a triple, recording separate brightness values for RGB(red, green, blue) components
# # then 2D array of pixels stored as 3D array of numeric values

