"""
Created on Tue Sep 21 07:33:28 2021

@author: Daniel
"""


import numpy as np
import skimage

def operacion_bandas(color_ban, ban_pan):

    return (color_ban + ban_pan) * 0.5

im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')
n = int(im_multi.shape[2])
listaunion = []
pan_float = im_pan.astype(np.float32)

print("Se sacarán " + str(n) + " bandas")

i=0
while i < n:
    matrix = im_multi[:,:,i]
    matrixfloat = matrix.astype(np.float32)
    fusionbandas = operacion_bandas (matrixfloat, pan_float)
    union = fusionbandas.astype(np.uint8)
    listaunion.append(union)
    i=i+1

i = i-1
fusioned_image = np.stack((listaunion),axis = 2)
t = skimage.io.imsave('prueba_ciclo.tif',fusioned_image, plugin='tifffile')
