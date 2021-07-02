import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


def file_to_array(name):
    """takes a 2D data set with columns of the same data separated by tabs, and each new piece of data within a set a
    line below the previous point. returns the data in a 2D array by row, then by column
    """
    file_data = open(name, 'r').read()
    data = [x.split() for x in file_data.split('\n')]   # making 2D array out of data, by line and then by white space
    return data

def create_one_row(width):
    """returns one row of zeros of width "width"...
    """
    row = []
    for col in range(width):
        row += [0]
    return row


def create_array(width, height):
    """returns an array of zeros of width 'width' and height 'height'
    """
    array = []
    for row in range(height):
        array += [create_one_row(width)]
    return array


def reverse(array):
    """takes a two dimensional array and the index to the specific list reversed as the argument and reverses the order
    of all elements within it. returns the reversed list
    """
    new_array = create_array(len(array[0]), len(array))
    for i in range(len(array)):
        for j in range(len(array[i])):
            new_array[i][j] = array[i][-1-j]
    return new_array


def transpose(a):           # some error in this function or the use of this function
    """transpose takes a matrix a and makes all the columns into rows
    and all of the rows into columns. Then transpose returns the matrix
    """
    b = create_array(len(a), len(a[0]))
    for row in range(len(a)):
        for col in range(len(a[row])):
            b[col][row] = a[row][col]
    return b

def data_handling_milan(filename='milankovitch.data.txt'):
    data_array = file_to_array(filename)[1:]        # cutting off the first line of the file
    data_array = transpose(data_array)              # transposing the array to make innermost list each column of data
    data_array = np.array(data_array)
    data_array = data_array.astype(float)
    for i in range(len(data_array[2])):
        data_array[0][i] *= 1000
    return data_array


def data_handling_la2004(filename='INSOLN.LA2004.BTL.250.ASC'):
    data_array = file_to_array(filename)        # cutting off the first line of the file
    data_array = transpose(data_array)          # transposing the array to make innermost list each column of data
    data_array = np.array(data_array)
    data_array = data_array.astype(float)
    return data_array


def data_handling_vostok(filename='vostok_ice_core_data.txt'):
    data_array = file_to_array(filename)
    data_array = transpose(data_array)
    data_array = np.array(data_array)
    data_array = data_array.astype(float)
    for i in range(len(data_array[2])):
        data_array[2][i] *= -1
    return data_array


data_array = []
dataset = input('which dataset would you like to sonify? Filename:')
if dataset == 'milankovitch':
    data_array = data_handling_milan()
elif dataset == 'la2004':
    data_array = data_handling_la2004()


data_array2 = []
data_array2 = data_handling_vostok()

# style.use('dark_background')

t = data_array[0] # time data or equivalent linspace
t2 = data_array2[2]


y1 = data_array[1] # eccentricity data
y2 = 180*data_array[2]/np.pi # obliquity data
y3 = data_array[1]*np.sin(data_array[3]) # precession data
y4 = data_array2[3] # ice core data

fig = plt.figure(figsize=(17,9.5))    # creating instance of type Figure

plt.subplot(4, 1, 1)
plt.plot(t, y1, '.-', linewidth = .5, markersize = .2)
plt.title(dataset + ' data')
plt.ylabel('eccentricity')

plt.subplot(4, 1, 2)
plt.plot(t, y2, '.-', linewidth = .5, markersize = .2)
plt.ylabel('obliquity')

plt.subplot(4, 1, 3)
plt.plot(t, y3, '.-', linewidth = .5, markersize = .2)
plt.ylabel('precession')
  
plt.subplot(4, 1, 4)
plt.plot(t2, y4, '.-', linewidth = .5, markersize = .2)
plt.ylabel('temperature')
plt.xlabel('time (yrs)')


plt.show()
