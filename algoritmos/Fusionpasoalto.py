# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 06:48:17 2021

@author: Daniel
"""

import numpy as np
import skimage
from scipy import ndimage

filtro1 = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]]) * (1/9)
filtro2 = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]]) * (1/9)


def fusion_paso_alto(banda,im1, im2):
    fusionbanda = banda + np.multiply(np.divide(banda, im2), im1)
    return fusionbanda

def fusion_paso_alto_cpu(im_multi, im_pan):
    
    listaunion = [] 
    n_bandas = int(im_multi.shape[2])
    double_pan = im_pan.astype(np.float32)

    imagen1 = ndimage.correlate(double_pan, filtro1, mode='constant')
    imagen2 = ndimage.correlate(double_pan, filtro2, mode='constant')

    imagen1[imagen1<0] = 0
    imagen2[imagen2<0] = 0

    imagen1 = imagen1.astype(np.uint8)
    imagen2 = imagen2.astype(np.uint8)

    double_imagen1 = imagen1.astype(np.float32)
    double_imagen2 = imagen2.astype(np.float32)
    i = 0
    
    while i < n_bandas:
        banda = im_multi[:,:,i]
        bandafloat = banda.astype(np.float32)
        fusionbandas = fusion_paso_alto(bandafloat, double_imagen1, double_imagen2)
        fusionbandas[fusionbandas>255] = 255
        to_image = fusionbandas.astype(np.uint8)
        listaunion.append(to_image)
        i = i + 1

    fusioned_image = np.stack((listaunion),axis = 2)
    return fusioned_image




"""

double_pan = im_pan.astype(np.float32)

imagen1 = ndimage.correlate(double_pan, filtro1, mode='constant')
imagen2 = ndimage.correlate(double_pan, filtro2, mode='constant')


imagen1[imagen1<0] = 0
imagen2[imagen2<0] = 0

imagen1 = imagen1.astype(np.uint8)
imagen2 = imagen2.astype(np.uint8)


double_imagen1 = imagen1.astype(np.float32)
double_imagen2 = imagen2.astype(np.float32)


b_red = im_multi[:,:,0]
b_green = im_multi[:,:,1]
b_blue = im_multi[:,:,2]

b_red1 = b_red.astype(np.float32)
b_green1 = b_green.astype(np.float32)
b_blue1 = b_blue.astype(np.float32)

fusionbanda1 = b_red1 + np.multiply(np.divide(b_red1, double_imagen2), double_imagen1)
fusionbanda2 = b_green1 + np.multiply(np.divide(b_green1, double_imagen2), double_imagen1)
fusionbanda3 = b_blue1 + np.multiply(np.divide(b_blue1, double_imagen2), double_imagen1)

#funncion
fusionbanda1[fusionbanda1>255] = 255
fusionbanda2[fusionbanda2>255] = 255
fusionbanda3[fusionbanda3>255] = 255

fusionbanda11 = fusionbanda1.astype(np.uint8)
fusionbanda22 = fusionbanda2.astype(np.uint8)
fusionbanda33 = fusionbanda3.astype(np.uint8)

fusioned_image = np.stack((fusionbanda11, fusionbanda22, fusionbanda33),axis=2)

t = skimage.io.imsave('prueba2fusionpasoalto.tif',fusioned_image, plugin ='tifffile')

"""

