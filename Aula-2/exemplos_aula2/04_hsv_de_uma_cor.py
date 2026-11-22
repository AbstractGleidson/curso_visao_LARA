import cv2
import numpy as np

# cada cor como uma "imagem" de 1 x 1 pixel, em BGR
cores = {'vermelho': [0, 0, 255], 'verde': [0, 255, 0], 'azul': [255, 0, 0],
         'amarelo': [0, 255, 255]}

for nome, bgr in cores.items():
    pixel = np.uint8([[bgr]])
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
    print(f'{nome:9s} BGR = {bgr} -> HSV = {hsv[0, 0]}')
