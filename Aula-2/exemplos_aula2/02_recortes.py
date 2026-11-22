import cv2

imagem = cv2.imread('imagens/foto4.jpg')

# recorte de 72 x 72 pixels em volta da bola vermelha
recorte = imagem[298:370, 375:447]
print('Dimensões do recorte:', recorte.shape)

# o recorte é uma visão da imagem: alterar um altera o outro
recorte[:, :] = (0, 0, 0)
print('Pixel da imagem depois de pintar o recorte:', imagem[334, 411])

# para trabalhar de forma independente, copie
imagem = cv2.imread('imagens/foto4.jpg')
copia = imagem[298:370, 375:447].copy()
copia[:, :] = (0, 0, 0)
print('Pixel da imagem depois de pintar a cópia  :', imagem[334, 411])
