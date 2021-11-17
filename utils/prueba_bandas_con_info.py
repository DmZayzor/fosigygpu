# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:28:57 2021

@author: Daniel
"""

import skimage.io
import numpy as np
import matplotlib.pyplot as plt

i=0
band_list = []
test_multi_con_info = skimage.io.imread('multi_con_info.tif', plugin='tifffile')
bands = test_multi_con_info.shape[2]
while i < bands:
    banda = test_multi_con_info[:,:,i]
    banda_float = banda.astype(np.float32)
    print("aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",banda)
    #banda_color = crear_color(banda_float,name)
    banda_imagen = banda_float.astype(np.uint8)
    band_list.append(banda_imagen)
    i=i+1
