# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 18:40:28 2021

@author: Daniel
"""
#Fusion Gram

import skimage
import numpy as np

im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')

pan_float = []
lista_bandas = []
N = []
n_bandas = 0


#def fusion_gram_cpu(im_multi, im_pan):
    #print("print de prueba linea 20 " )
    
pan_float = im_pan.astype(np.float32)
fusion = pan_float
i_multi = im_multi
n_bandas = int(im_multi.shape[2])


#("n_bandas en fusion_gram_cpu vale ", n_bandas )
#fusionar_bandas(fusion, i_multi)
    
    #return fusion

#def fusionar_bandas(fusion, i_multi):
    
i = 0
n_bandas = int(i_multi.shape[2])
#print("-----------------------------------------" , np.shape(i_multi))
 
lista_bandas = []

#print("n_bandas en fusionar_bandas vale " , n_bandas)

while i < n_bandas:
    banda = i_multi[:,:,i]
    banda_float = banda.astype(np.float32)
    fusion = fusion + banda_float
    banda_float = banda_float.astype(np.uint8)
    lista_bandas.append(banda_float)
    #print("que s hay aquí ??????????    ",lista_bandas[:,:,i])
    i=i+1
    
#print("print de prueba linea 43 " )   
  
fusion_prom = fusion / 4
lista_bandas.insert(0, fusion_prom)

#print("el tipo de dato es    ", type(lista_bandas))

fusioned_image = np.stack((lista_bandas),axis = 2)

    
N = int(fusioned_image.shape[2])

n = 0
m = 1

k = 0
r = []
numerador = 0
denominador = 0

for n in range(N):
   
    matriz_temp = fusioned_image[:,:,0:n+1]
    
    for m in range(n):
        numerador = numerador + (fusioned_image[:,:,n] * matriz_temp[:,:,m])
        denominador = denominador + (matriz_temp[:,:,m] * matriz_temp[:,:,m])
        r.append(numerador/denominador)
        matriz_temp[:,:,n] = matriz_temp[:,:,n] - r[k] * matriz_temp[:,:,m]
        k = k + 1
    
"""
    for n in range(N):
      
        
        #u[:,:,n] = lista_bandas[:,:,n].astype(np.float32)
        valor_banda = lista_bandas[:,:,n]
        
        valor_banda = valor_banda.astype(np.float32)
        
        for m in n-1:
            numerador = numerador + (fusioned_image[:,:,n] * u[:,:,m])
            denominador = denominador + (u[:,:,m] * u[:,:,m])
            k = k + 1
            r[k] = numerador/denominador
            u[:,:,n] = u[:,:,n] - r[k] * u[:,:,m]
    #return u

def fusion_bandas2():
    j = 2
    lista_imagen = []
    lista_bandas2 = []
    r = []
    u = []
    k = 0
    n = 1
    m = 1

    while j < n_bandas:
        imagen = u[:,:,j]
        lista_imagen.append(imagen)
        j = j + 1
        lista_imagen =lista_imagen + pan_float
        u = np.stack((lista_imagen),axis = 2)
        [M,B,N] = u.size
        for n in N:
            lista_bandas2[:,:,n] = u[:,:,n]
            for m in n-1:
                k = k + 1
                lista_bandas2[:,:,n] = lista_bandas2[:,:,n] + r[k] * u[:,:,m]
        fusion_gram(lista_bandas2)

def fusion_gram(lista_bandas2):
    l = 2
    lista_finales = []
    while l < n_bandas:
        imagen_final = lista_bandas2[:,:,l]
        imagen_final = imagen_final.astype(np.float32)
        lista_finales.append(imagen_final)
        l = l + 1
    f_gram = np.stack((lista_finales),axis = 2)
    return f_gram
"""

#Fusion Gram
"""
import skimage
import numpy as np

#im_pan = skimage.io.imread('pan8r.tif', plugin='tifffile')
#im_multi = skimage.io.imread('rgb81r.tif', plugin='tifffile')
pan_float = []

n_bandas = 0


def fusion_gram_cpu(im_multi, im_pan):
    print("print de prueba linea 20 " )
    pan_float = im_pan.astype(np.float32)
    fusion = pan_float
    i_multi = im_multi
    n_bandas = int(im_multi.shape[2])
    print("n_bandas en fusion_gram_cpu vale ", n_bandas )
    fusionar_bandas(fusion, i_multi)
    
    #return fusion

def fusionar_bandas(fusion, i_multi):
    i = 0
    n_bandas = int(i_multi.shape[2])
    lista_bandas = []
    print("n_bandas en fusionar_bandas vale " , n_bandas)
    while i < n_bandas:
        banda = i_multi[:,:,i]
        banda_float = banda.astype(np.float32)
        fusion = fusion + banda_float
        banda_float = banda_float.astype(np.uint8)
        lista_bandas.append(banda_float)  
        i=i+1
    print("print de prueba linea 43 " )     
    fusion_prom = fusion / 4
    lista_bandas.append(fusion_prom)
    fusioned_image = np.stack((lista_bandas),axis = 2)
    print("print de prueba linea 47 " )
    print("zzzzzzzzzzzzzzzzzzzzzz" , lista_bandas.shape)
    fusionar_imagen(fusioned_image)    

def fusionar_imagen(fusioned_image):
    print("print de prueba linea 52")
    
    [M,B,N] = np.shape(fusioned_image)
    
    n = 1
    m = 1
    u = []
    k = 0
    r = []
    numerador = 0
    denominador = 0

    for n in N:
        u[:,:,n] = fusioned_image[:,:,n]
        for m in n-1:
            numerador = numerador + (fusioned_image[:,:,n] * u[:,:,m])
            denominador = denominador + (u[:,:,m] * u[:,:,m])
            k = k + 1
            r[k] = numerador/denominador
            u[:,:,n] = u[:,:,n] - r[k] * u[:,:,m]
    #return u

def fusion_bandas2():
    j = 2
    lista_imagen = []
    lista_bandas2 = []
    r = []
    u = []
    k = 0
    n = 1
    m = 1

    while j < n_bandas:
        imagen = u[:,:,j]
        lista_imagen.append(imagen)
        j = j + 1
        lista_imagen =lista_imagen + pan_float
        u = np.stack((lista_imagen),axis = 2)
        [M,B,N] = u.size
        for n in N:
            lista_bandas2[:,:,n] = u[:,:,n]
            for m in n-1:
                k = k + 1
                lista_bandas2[:,:,n] = lista_bandas2[:,:,n] + r[k] * u[:,:,m]
        fusion_gram(lista_bandas2)

def fusion_gram(lista_bandas2):
    l = 2
    lista_finales = []
    while l < n_bandas:
        imagen_final = lista_bandas2[:,:,l]
        imagen_final = imagen_final.astype(np.float32)
        lista_finales.append(imagen_final)
        l = l + 1
    f_gram = np.stack((lista_finales),axis = 2)
    return f_gram
#funcion 5

"""

