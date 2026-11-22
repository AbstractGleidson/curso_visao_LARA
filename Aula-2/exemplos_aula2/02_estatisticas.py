import cv2
import numpy as np

imagem = cv2.imread('imagens/foto8.jpg')

# quadrado de 15 x 15 pixels dentro da bola, centrado em (u, v) = (340, 332)
u, v = 340, 332
amostra = imagem[v - 7:v + 8, u - 7:u + 8]
pixels = amostra.reshape(-1, 3)        # 225 linhas (pixels) por 3 colunas (B, G, R)

print('Forma da amostra :', amostra.shape)
print('Forma após reshape:', pixels.shape)
print('Média por canal  :', np.mean(pixels, axis=0).round(1))
print('Mediana por canal:', np.median(pixels, axis=0))

# a armadilha do uint8: a soma "dá a volta" depois de 255
a = np.uint8(200)
b = np.uint8(100)
print('uint8 200 + 100 =', np.array([a]) + np.array([b]))
print('float 200 + 100 =', float(a) + float(b))
