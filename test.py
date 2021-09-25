# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:31:01 2021

@author: Daniel
"""
import skimage
import numpy as np
from algoritmos import ValorMedio as vm
from algoritmos import Fusionpasoalto as fpa

im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')

fusio_valor_medio = vm.fusion_valor_medio_cpu(im_multi, im_pan)
t = skimage.io.imsave('prueba_test.tif',fusio_valor_medio, plugin ='tifffile')

fusion_paso_alto = fpa.fusion_paso_alto_cpu(im_multi, im_pan)
t = skimage.io.imsave('fusion_paso_alto.tif',fusion_paso_alto, plugin ='tifffile')