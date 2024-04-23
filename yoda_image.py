from PIL import Image
from PIL import ImageShow
import numpy as np


def double_threshhold(array, threshhold_1=85, threshhold_2=127):
    array = np.mean(array, axis=2)
    array[array < threshhold_1] = 0
    array[array >= threshhold_2] = 255
    for i in range(np.shape(array)[0]):
        for j in range(np.shape(array)[1]):
            result = array[i, j]
            if result < threshhold_2 and result >= threshhold_1:
                array[i, j] = 127
    return array

def single_threshhold(array, threshhold_1=127):
    array = np.mean(array, axis=2)
    array[array < threshhold_1] = 0
    array[array != 0] = 255
    return array


im = Image.open("yoda.jpeg")
a = np.asarray(im)
threshhold_1 = 85
threshhold_2 = 170
a = single_threshhold(a, threshhold_1)
im1 = Image.fromarray(a)
ImageShow.show(im1)

