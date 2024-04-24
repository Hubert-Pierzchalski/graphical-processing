from PIL import Image, ImageOps
from PIL import ImageShow
import numpy as np
from math import ceil
import matplotlib.pyplot as plt


def double_threshhold(array, threshhold_1=85, threshhold_2=127):
    array = np.mean(array, axis=2)
    array[array < threshhold_1] = 0
    array[array >= threshhold_2] = 0
    for i in range(np.shape(array)[0]):
        for j in range(np.shape(array)[1]):
            result = array[i, j]
            if result < threshhold_2 and result >= threshhold_1:
                array[i, j] = 255
    return array

def single_threshhold(array, threshhold_1=127):
    array = np.mean(array, axis=2)
    array[array < threshhold_1] = 0
    array[array != 0] = 255
    return array

def contrast_enchancment(array):
    array = np.mean(array, axis=2, dtype=int)
    # cdf = np.empty([256])
    # for i in range(256):
    #     cdf[i] = np.sum(array == i)
    # plot_to_cdf(cdf)
    # return array
    number_of_pixels = np.shape(array)[0] * np.shape(array)[1]
    probability = np.empty([256])
    for i in range(256):
        probability[i] = (np.sum(array == i))/number_of_pixels
    cdf = np.cumsum(probability) #32-36 is creating a function that will equalize histogram
    for i in range(np.shape(array)[0]):
        for j in range(np.shape(array)[1]):
            array[i][j] = ceil(cdf[round(array[i][j])] * 255) #We use histogram euqaliztion function to boost contrast in picture

    show_plot(array, number_of_pixels) #Proof that light values are now equally distributed showd as cdf
    return array

def show_plot(array, number_of_pixels):
    y = np.empty([256])
    for i in range(256):
        y[i] = (np.sum(array == i))/number_of_pixels
    y = np.cumsum(y)
    x = np.arange(0, 256, 1, dtype=int)
    fig = plt.figure()
    plt.plot(x,y)
    plt.show()


im = Image.open("yoda.jpeg")
a = np.asarray(im)

#for grayscale
# threshhold_1 = 85
# threshhold_2 = 170
# grayscale_array = single_threshhold(a, threshhold_1)
# im1 = Image.fromarray(grayscale_array)
# ImageShow.show(im1)
gray_scale = np.mean(a, axis=2)
im1 = Image.fromarray(gray_scale)
ImageShow.show(im1)
contrast_arr = contrast_enchancment(a)
im2 = Image.fromarray(contrast_arr)
ImageShow.show(im2)




# contrast_array = contrast_enchancment(a)
# im2 = Image.fromarray(contrast_array)
# ImageShow.show(im2)