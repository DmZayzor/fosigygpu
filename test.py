# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:31:01 2021
@author: Daniel
"""
import skimage.io
from PIL import Image
from algoritmos import crear_images as ci
from algoritmos import fusion_valor_medio as vm
from osgeo import gdal
#from algoritmos import fusion_paso_alto as fpa
#from algoritmos import fusion_gram as fg
#from algoritmos import fusion_hpf as fh
#from algoritmos import pixel_cut as pc
#from metricas import measures as ms
#from utils import utilidades as utl


inicial_rgb = skimage.io.imread('rgbikonos.tif', plugin='tifffile')
data_rgb = gdal.Open("rgbikonos.tif")
inicial_pan = skimage.io.imread('ikonospanrecorte.tif', plugin='tifffile')
data_pan = gdal.Open("ikonospanrecorte.tif")
pixel_multiplicado,origen,pixel=ci.crear_imagenes(inicial_rgb,data_rgb,inicial_pan,data_pan)

multi = skimage.io.imread('multi.tif', plugin='tifffile')
rgb_gualada = ci.igualar_rgb(multi,pixel)
dibujar_rgb_igualada = skimage.io.imsave('rgb_igualada.tif',rgb_gualada, plugin ='tifffile')

rgb=Image.open("rgb_igualada.tif")
xIntrinsic, yIntrinsic, H, W = ci.dibujar_recuadro(rgb)

rgb_rec = ci.recortar_rgb(xIntrinsic,yIntrinsic,origen,pixel_multiplicado,H,W,pixel,rgb)
dibujar_rgb_rec = skimage.io.imsave('multirec.tif',rgb_rec, plugin ='tifffile')

pan=Image.open("pan8.tif")
pan_rec = ci.recortar_pan(xIntrinsic,yIntrinsic,origen,pixel_multiplicado,H,W,pixel,pan)
dibujar_rgb_rec = skimage.io.imsave('panrec.tif',pan_rec, plugin ='tifffile')

recorte_rgb = skimage.io.imread('multirec.tif', plugin='tifffile')
recorte_pan = skimage.io.imread('panrec.tif', plugin='tifffile')
rgb_rec_final = ci.expandir_recorte_rgb(recorte_rgb,recorte_pan,pixel)
dibujar_rec_final_rgb = skimage.io.imsave('rgbdef.tif',rgb_rec_final, plugin ='tifffile')



im_pan = skimage.io.imread('panrec.tif', plugin='tifffile')
im_multi = skimage.io.imread('multirec.tif', plugin='tifffile')
multi = Image.open('multirec.tif')
pan = Image.open('panrec.tif')
pan.show()
multi.show()

fusio_valor_medio = vm.fusion_valor_medio_cpu(im_multi, im_pan)
t = skimage.io.imsave('fusion_valor_medio_parque_lago.tif',fusio_valor_medio, plugin ='tifffile')
im = Image.open('fusion_valor_medio_parque_lago.tif')
im.show()

#fusion_paso_alto = fpa.fusion_paso_alto_cpu(im_multi, im_pan)
#dibujar_fpa = skimage.io.imsave('fusion_paso_alto.tif',fusion_paso_alto, plugin ='tifffile')

#fusion_gram= fg.fusion_gram_cpu(im_multi, im_pan)
#dibujar = skimage.io.imsave('fusion_gram.tif',fusion_gram, plugin ='tifffile')

#fusion_hpf = fh.fusion_hpf_cpu(im_pan,im_multi)
#dibujar = skimage.io.imsave('fusion_HPF_cpu.tif',fusion_hpf, plugin ='tifffile')
#hpf = skimage.io.imread('fusion_articulo_HPF.tif', plugin='tifffile')

#mse = ms.mse(hpf, im_multi)
#print("el vector mse es: " , mse)

#bias = ms.bias(hpf, im_multi)
#print("el vector bias es: " , bias)

#correlation_coeff = ms.correlation_coeff(hpf, im_pan)
#print("el vector coeff es: " , correlation_coeff)


#imagen, geo_info = utl.cargar_info('fusion_HPF_cpu.tif')


#new_multi = skimage.io.imread('rgbikonos.tif', plugin='tifffile')

#combinar = pc.fusionar(new_multi)
#dibujar = skimage.io.imsave('prueba_pancro.tif',combinar, plugin ='tifffile')

#print("prueba pancro creada")

