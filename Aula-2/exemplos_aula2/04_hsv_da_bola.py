import cv2
import numpy as np

imagem = cv2.imread('imagens/foto4.jpg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

pontos = {'bola vermelha': (421, 334), 'bola verde clara': (150, 400),
          'bola verde escura': (380, 520), 'parede': (450, 120), 'chão': (80, 600)}

for nome, (u, v) in pontos.items():
    amostra = hsv[v - 7:v + 8, u - 7:u + 8].reshape(-1, 3)
    h, s, val = np.median(amostra, axis=0)
    print(f'{nome:18s} H = {h:3.0f} | S = {s:3.0f} | V = {val:3.0f}')
