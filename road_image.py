from PIL import Image, ImageShow
import numpy as np
from scipy.signal import convolve2d
import time


def mask(array):
    kernel = np.ones((71, 71))
    grad = convolve2d(array, kernel, mode='same')
    grad /= (71 * 71)
    return grad

im = Image.open("road.jpg")
photo_array = np.asarray(im)
greyscale = np.mean(photo_array, axis=2)
start = time.perf_counter()
final_arr = mask(greyscale)
end = time.perf_counter()
print(end - start)
final_im = Image.fromarray(final_arr)
ImageShow.show(final_im)