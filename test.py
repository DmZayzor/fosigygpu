# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:31:01 2021
@author: Daniel
"""
import skimage.io

#from algoritmos import ValorMedio as vm
#from algoritmos import fusion_paso_alto as fpa
#from algoritmos import fusiongram as fg
from algoritmos import fusion_hpf as fh
#from metricas import measures as ms

im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')


#fusio_valor_medio = vm.fusion_valor_medio_cpu(im_multi, im_pan)
#t = skimage.io.imsave('fusion_valor_medio.tif',fusio_valor_medio, plugin ='tifffile')

#fusion_paso_alto = fpa.fusion_paso_alto_cpu(im_multi, im_pan)
#dibujar_fpa = skimage.io.imsave('fusion_paso_alto.tif',fusion_paso_alto, plugin ='tifffile')

#fusion_gram= fg.fusion_gram_cpu(im_multi, im_pan)
#dibujar = skimage.io.imsave('fusion_gram_algoritmosssss.tif',fusion_gram, plugin ='tifffile')

fusion_hpf = fh.fusion_hpf_cpu(im_pan,im_multi)
dibujar = skimage.io.imsave('fusion_articulo_HPF.tif',fusion_hpf, plugin ='tifffile')
#hpf = skimage.io.imread('fusion_articulo_HPF.tif', plugin='tifffile')

#mse = ms.mse(hpf, im_multi)
#print("el vector mse es: " , mse)

#bias = ms.bias(hpf, im_multi)
#print("el vector bias es: " , bias)

#correlation_coeff = ms.correlation_coeff(hpf, im_pan)
#print("el vector coeff es: " , correlation_coeff)
