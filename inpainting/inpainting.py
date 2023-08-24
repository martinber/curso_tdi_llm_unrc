#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def grad_x(img):
    """Gradiente o derivada de la imagen en eje X: d/dx"""
    return np.gradient(img, axis=1)


def grad_y(img):
    """Gradiente o derivada de la imagen en eje Y: d/dy"""
    return np.gradient(img, axis=0)


def divergence(field_x, field_y):
    """Divergencia de un campo vectorial: ∇"""
    return grad_x(field_x) + grad_y(field_y)


def threshold(img, threshold):
    """Convierte a 1 todos los pixeles mayores al threshold y en 0 al resto"""
    return np.where(img >= threshold, 1, 0)


def open_image(filename):
    """Cargar una imagen"""
    return np.asarray(Image.open(filename))[:, :, 0] / 255


def laplacian(img):
    """Laplaciano de una imagen: Δ"""
    # [HACER] Escribir la función acá para devolver el laplaciano en vez de img
    return img


# Cargar imagen y hacer una copia

img_original = open_image("./unrc.png")
img = img_original.copy()

# Inicio de nuestro impainting

mask = img

# [HACER] Modificar mask para que tenga 1 en todos lados menos en donde está el texto

# [HACER] Hacer un for loop que de 50 vueltas y que adentro tenga la ecuación
# [HACER] Usar lambda = 2 y alfa = 0.5

# Mostrar imagenes:

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.set_title("img_original")
ax1.imshow(img_original, vmin=0, vmax=1, cmap="gray")
ax2.set_title("mask")
ax2.imshow(mask, vmin=0, vmax=1, cmap="gray")
ax3.set_title("img")
ax3.imshow(img, vmin=0, vmax=1, cmap="gray")
# ax4.set_title("...")
# ax4.imshow(..., vmin=0, vmax=1, cmap="gray")
plt.show()
