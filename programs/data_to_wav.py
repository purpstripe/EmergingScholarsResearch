
# http://hplgit.github.io/primer.html/doc/pub/diffeq/._diffeq-solarize
# d002.html
# https://www.youtube.com/watch?v=_VtCoeMZ5nc
# https://www.youtube.com/watch?v=X6K5hBTKcLs
# https://cimss.ssec.wisc.edu/wxfest/Milankovitch/earthorbit.html

# new data set: http://vo.imcce.fr/insola/earth/online/earth/earth.html
# and info: https://www.aanda.org/articles/aa/full/2004/46/aa1335/aa1335.html

# https://www.youtube.com/watch?v=H-iCZElJ8m0
# https://www.audiocheck.net/soundtests_nonlinear.php

# https://www.youtube.com/ watch?v=ZD8THEz18gc&index=71&list=PL2186CFB2CE12A8B5


import numpy as np
import scipy.io.wavfile as wavfile


def array_to_file(name, data):
    f = open(name, 'w')
    f2 = open(name+'2', 'w')
    for i in range(len(data)//2):
        f.write(str(data[i]))
        f.write('\n')
    for j in range(len(data)//2):
        f2.write(str(data[j+len(data)//2]))
        f.write('\n')
    f.close()


def sin_wave_array_t(frequency, length, amplitude=1, sample_rate=44100):
    """takes frequency, length, and sets a default for amplitude and sample rate to
    generate an array of float data representing a note (from the sin wave) s(t)=Asin(2πft).
    """
    time_points = np.arange(1, length, 1/sample_rate)
    y = np.sin(2 * np.pi * frequency * time_points)
    y = amplitude * y
    return y


def sin_wave_array_p(frequency, periods, amplitude=1, sample_rate=44100):       # is the answer to the higher freq here?
    """takes frequency, length, and sets a default for amplitude and sample rate to
    generate an array of float data representing a note (from the sin wave) s(t)=Asin(2πft).
    """
    length = periods/frequency
    time_points = np.arange(1, length, 1/sample_rate)
    y = np.sin(2 * np.pi * frequency * time_points)
    y = amplitude * y
    return y


def fourier_wave_array(frequency, length, sample_rate=44100):
    """takes frequency, length, and sets a default for sample rate to generate an array of
    float data representing a note with the first three fourier coefficients of a square wave"""
    n = int(1/frequency * sample_rate)  # samples per period
    y = [0] * n
    for i in range(n):
        y1 = 4 / np.pi * np.sin(2 * np.pi * i / n)          # first fourier transform wave
        y2 = 4 / (3 * np.pi) * np.sin(6 * np.pi * i / n)    # second fourier transform wave
        y3 = 4 / (5 * np.pi) * np.sin(10 * np.pi * i / n)   # third fourier transform wave
        y[i] = y1 + y2 + y3
    periods = int(round((length * sample_rate) / n))
    y = np.tile(y, periods)     # y = y * periods
    return y


def square_wave_array(frequency, length, sample_rate=44100):
    """takes frequency, length, and sets a default for sample rate to
    generate an array of float data representing a note with a square wave"""
    n = int(1/frequency * sample_rate)  # samples per period
    y = [0] * n
    for i in range(n):
        if i < n / 2:
            y[i] = 1
        else:
            y[i] = -1
    periods = int(round((length * sample_rate) / n))
    y = np.tile(y, periods)     # y = y * periods
    return y


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


def reverse(array, i):
    """takes a two dimensional array and the index to the specific list reversed as the argument and reverses the order
    of all elements within it. returns the reversed list
    """
    new_array = create_array(len(array[i]), len(array))
    for j in range(len(array[i])):
        new_array[i][j] = array[i][-1-j]
    return new_array[i]


def transpose(a):
    """transpose takes a matrix a and makes all the columns into rows
    and all of the rows into columns. Then transpose returns the matrix
    """
    b = create_array(len(a), len(a[0]))
    for row in range(len(a)):
        for col in range(len(a[row])):
            b[col][row] = a[row][col]
    return b


def is_column_not_equal(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            print(str(i))
            return True
    return False


def are_arrays_equal(a, b):
    for i in range(len(a)):
        if is_column_not_equal(a[i], b[i]):
            print(str(i))


def generate_wave_file(name, data, sample_rate=44100):
    """takes the name of wav file to be written, the data required to write the file, and the sample rate at
    which to sample the data and creates the appropriate wav file
    """
    max_of_list = max(np.absolute(data))
    for element in range(len(data)):
        # normalization for write function that clips for any values y < -1 or y > 1
        data[element] = data[element] / max_of_list
    wavfile.write(name, sample_rate, np.array(data))


# TODO check these methods to make sure they are working properly!!!


def data_to_lin_amp(data):
    frequency = 220
    amp_period = 640    # number of points per each amplitude determined by the data
    total_num_points = amp_period * len(data)  # needs to be a multiple of the length of the data set for even amp ∆s
    sample_rate = int(round(total_num_points/3600))
    length = total_num_points/sample_rate
    points = sin_wave_array_t(frequency, length, 1)
    max_of_list = max(np.absolute(data))
    for i in range(len(data)):
        amplitude = data[i]/max_of_list
        for point in range(amp_period):
            points[point + amp_period * i] *= amplitude
    return np.array(points)


def data_to_exp_amp(data):
    frequency = 220
    amp_period = 640    # number of points per each amplitude determined by the data
    total_num_points = amp_period * len(data)  # needs to be a multiple of the length of the data set for even amp ∆s
    sample_rate = int(round(total_num_points/3600))
    length = total_num_points/sample_rate
    points = sin_wave_array_t(frequency, length, 1)
    max_of_list = max(np.absolute(data))
    k = 2
    for i in range(len(data)):
        exp = data[i]/max_of_list
        amplitude = (k ** exp)/k
        for point in range(amp_period):
            points[point + amp_period * i] *= amplitude
    return np.array(points)


def data_to_lin_freq(data, sample_rate=44100):
    amplitude = 1
    periods = 30
    max_freq = 5000
    min_freq = 100
    max_of_list = max(np.absolute(data))
    y = []
    for element in data:
        frequency = int(round((max_freq - min_freq) * element/max_of_list)) + min_freq
        points = sin_wave_array_p(frequency, periods, amplitude, sample_rate)
        for point in points:
            y.append(point)
    return np.array(y)


def data_to_exp_freq(data, sample_rate=44100):
    amplitude = 1
    periods = 30
    max_freq = 20000
    min_freq = 100
    max_of_list = max(np.absolute(data))
    y = []
    for element in data:
        frequency = int(round((max_freq - (min_freq - 1)) ** (element/max_of_list) + (min_freq - 1)))
        points = sin_wave_array_p(frequency, periods, amplitude, sample_rate)
        for point in points:
            y.append(point)
    return np.array(y)


# TODO add these methods to main() and test them!
def data_to_lin_freq_and_amp(freq_data, amp_data, sample_rate=44100):
    periods = 30
    max_freq = 5000
    min_freq = 100
    max_of_freq_list = max(np.absolute(freq_data))
    max_of_amp_list = max(np.absolute(amp_data))
    y = []
    for i in range(len(freq_data)):
        frequency = int(round((max_freq - min_freq) * freq_data[i] / max_of_freq_list)) + min_freq
        amplitude = amp_data[i]/max_of_amp_list
        points = sin_wave_array_p(frequency, periods, amplitude, sample_rate)
        for point in points:
            y.append(point)
    return np.array(y)


def data_to_exp_freq_and_amp(freq_data, amp_data, sample_rate=44100):
    periods = 30
    max_freq = 20000
    min_freq = 100
    max_of_freq_list = max(np.absolute(freq_data))
    max_of_amp_list = max(np.absolute(amp_data))
    k = 2
    y = []
    for i in range(len(freq_data)):
        frequency = int(round((max_freq - (min_freq - 1)) ** (freq_data[i] / max_of_freq_list) + (min_freq - 1)))
        exp = amp_data[i] / max_of_amp_list
        amplitude = (k ** exp) / k
        points = sin_wave_array_p(frequency, periods, amplitude, sample_rate)
        for point in points:
            y.append(point)
    return np.array(y)


def data_handling_milan(index, filename='milankovitch.data.txt'):
    data_array = file_to_array(filename)[1:]        # cutting off the first line of the file
    data_array = transpose(data_array)              # transposing the array to make innermost list each column of data
    data_array = np.array(data_array)
    data_array = data_array.astype(float)
    if index == 2:
        for i in range(len(data_array[index])):
            data_array[index][i] = 180*data_array[index][i]/np.pi
    elif index == 3:
        for i in range(len(data_array[index])):
            data_array[index][i] = data_array[1][i]*np.sin(data_array[index][i])
    return data_array[index]


def data_handling_la2004(index, filename='INSOLN.LA2004.BTL.250.ASC'):
    data_array = file_to_array(filename)        # cutting off the first line of the file
    data_array = transpose(data_array)          # transposing the array to make innermost list each column of data
    data_array[index] = reverse(data_array, index)  # reversing the order of the backwards elements in specified column
    data_array = np.array(data_array)
    data_array = data_array.astype(float)
    if index == 2:
        for i in range(len(data_array[index])):
            data_array[index][i] = 180*data_array[index][i]/np.pi
    elif index == 3:
        for i in range(len(data_array[index])):
            data_array[index][i] = data_array[1][i]*np.sin(data_array[index][i])
    return data_array[index]


def main():
    dataset = input('which dataset would you like to sonify? Filename:')
    if dataset == 'milankovitch':
        subset = input('which subset would you like to sonify?' + '\n' + 'eccentricity' + '\n' + 'obliquity'
                       + '\n' + 'perihelion' + '\n' + 'insolation' + '\n' + 'global insolation' + '\n')
        if subset == 'eccentricity':
            index = 1
        elif subset == 'obliquity':
            index = 2
        elif subset == 'precession':
            index = 3
        elif subset == 'insolation':
            index = 4
        elif subset == 'global insolation':  # this, along with ice core data be used to approx. temp and ice caps
            index = 5
        else:
            index = 0
        method = input('which method would you like to use for sonification?' + '\n' + 'linamp' + '\n' +
                       'expamp' + '\n' + 'linfreq' + '\n' + 'expfreq')
        data_array = data_handling_milan(index)
    elif dataset == 'la2004':
        subset = input('which subset would you like to sonify?' + '\n' + 'eccentricity' + '\n' + 'obliquity'
                       + '\n' + 'perihelion' + '\n')
        if subset == 'eccentricity':
            index = 1
        elif subset == 'obliquity':
            index = 2
        elif subset == 'precession':
            index = 3
        else:
            index = 0
            subset = 'time'
        method = input('which method would you like to use for sonification?' + '\n' + 'linamp' + '\n'
                       + 'expamp' + '\n' + 'linfreq' + '\n' + 'expfreq' + '\n'
                       + 'direct')
        data_array = data_handling_la2004(index)
    sample_rate = 44100
    if method == 'linamp':
        generate_wave_file(subset + dataset + '_lin_amp.wav', data_to_lin_amp(data_array), sample_rate)
    elif method == 'expamp':
        generate_wave_file(subset + dataset + '_exp_amp.wav', data_to_exp_amp(data_array), sample_rate)
    elif method == 'linfreq':
        generate_wave_file(subset + dataset + '_lin_freq.wav', data_to_lin_freq(data_array, sample_rate), sample_rate)
    elif method == 'expfreq':
        generate_wave_file(subset + dataset + '_exp_freq.wav', data_to_exp_freq(data_array, sample_rate), sample_rate)
    else:
        generate_wave_file(subset + dataset + '.wav', data_array, sample_rate)


main()
