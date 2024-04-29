from PIL import Image, ImageShow
import numpy as np
from scipy.signal import convolve2d
import time


def mask(array):
    kernel = np.ones((71, 71))
    grad = convolve2d(array, kernel, mode='same')
    grad /= (71 * 71)
    return grad


def summed_area(array):
    diamaters_of_an_array = np.shape(array)
    i = diamaters_of_an_array[0]
    j = diamaters_of_an_array[1]
    while i != 1:
        array[i - 1, 0] = np.sum(array[:i, 0])
        i -= 1
    while j != 1:
        array[0, j - 1] = np.sum(array[0, :j])
        j -= 1
    for i in range(1, diamaters_of_an_array[0]):
        for j in range(1, diamaters_of_an_array[1]):
            array[i, j] = array[i, j] + array[i, j - 1] + array[i - 1, j] - array[i - 1, j - 1]
    new_array = np.empty(diamaters_of_an_array)
    rows = diamaters_of_an_array[0] - 71
    cols = diamaters_of_an_array[1] - 71
    for i in range(71, rows):
        for j in range(71, cols):
            new_array[i, j] = array[i, j] + array[i-71, j-71] - array[i-71, j] - array[i, j - 71]

    return new_array // (71**2)


if __name__ == '__main__':
    im = Image.open("road.jpg")
    photo_array = np.asarray(im)
    greyscale = np.mean(photo_array, axis=2)
    # start = time.perf_counter()
    # final_arr = summed_area(greyscale)
    # end = time.perf_counter()
    # print(end - start)
    # final_im = Image.fromarray(final_arr)
    # ImageShow.show(final_im)
    start = time.perf_counter()
    final_arr = mask(greyscale)
    end = time.perf_counter()
    print(end - start)
    final_im = Image.fromarray(final_arr)
    ImageShow.show(final_im)