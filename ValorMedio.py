"""
Created on Tue Sep 21 07:33:28 2021

@author: Daniel
"""

import glob
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from io import BytesIO
from PIL import Image
import PIL, requests
import skimage
from skimage.filters.rank import entropy
from skimage.morphology import disk

def step_1(matrix_1, matrix_color, msuma_matrix):
    for m in range(matrix_1.shape[0]):
        for n in range(matrix_1.shape[0]):
            if (msuma_matrix[m,n] != 0):
                matrix_1[m,n] = (3*matrix_color[m,n])/msuma_matrix[m,n]
            else:
                matrix_1[m,n] = msuma_matrix[m,n]
    return matrix_1

def step_2(matrix_1, matrix_2, matrix_image_pan):
    for m in range(matrix_2.shape[0]):
        for n in range(matrix_2.shape[0]):
            matrix_2[m,n] = matrix_1[m,n]*matrix_image_pan[m,n]
    return matrix_2

def step_3(matrix_1):
    mat_max = np.amax(matrix_1)
    mat_min = np.amin(matrix_1)
    return mat_max, mat_min

def step_4(matrix_1, matrix_color, mat_max, mat_min):
    for m in range(matrix_color.shape[0]):
        for n in range(matrix_color.shape[0]):
            matrix_color[m,n] = (((matrix_1[m,n]-mat_min)*255)/(mat_max-mat_min))
    return matrix_color


im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
p1 = im_pan.astype(np.float32)


im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')
plt.imshow(im_multi)

m1 = im_multi.astype(np.float32)
r = im_multi[:,:,0]
r1 = r.astype(np.float32)
g = im_multi[:,:,1]
g1 = g.astype(np.float32)
b = im_multi[:,:,2]
b1 = b.astype(np.float32)
p1 = im_pan.astype(np.float32)
msuma = r1+g1+b1
m11 = np.zeros_like(r1)
m11 = step_1(m11, r1, msuma)
m22 = np.zeros_like(g1)
m22 = step_2(m11, m22, p1)
m33 = np.zeros_like(b1)
m33 = step_1(m33, b1, msuma)
m44 = np.zeros_like(b1)
m44 = step_2(m33, m44, p1)
m55 = np.zeros_like(g1)
m55 = step_1(m55, g1, msuma)
m66 = np.zeros_like(g1)
m66 = step_2(m55, m66, p1)
Amax, Amin = step_3(m22)
rr = np.zeros_like(r1)
rr = step_4(m22, rr, Amax, Amin)
Amax, Amin = step_3(m66)
gg = np.zeros_like(g1)
gg = step_4(m66, gg, Amax, Amin)
Amax, Amin = step_3(m44)
bb = np.zeros_like(b1)
bb = step_4(m44, bb, Amax, Amin)
rrr = rr.astype(np.uint8)
ggg = gg.astype(np.uint8)
bbb = bb.astype(np.uint8)

# Combina las bandas resultantes
fusioned_image = np.stack((rrr, ggg, bbb),axis=2)
t = skimage.io.imsave('broveycpu_image.tif',fusioned_image, plugin='tifffile')


