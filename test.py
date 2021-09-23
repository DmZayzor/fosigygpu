# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:31:01 2021

@author: Daniel
"""
import skimage
import numpy as np
from algoritmos import ValorMedio as vm

im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')

fusioned_image = vm.fusion_valor_medio_cpu(im_multi, im_pan)
t = skimage.io.imsave('prueba_test.tif',fusioned_image, plugin ='tifffile')
