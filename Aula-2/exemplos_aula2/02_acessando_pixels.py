import cv2

imagem = cv2.imread('imagens/foto4.jpg')

# pixel na coluna u = 411 e na linha v = 334 (dentro da bola vermelha)
u, v = 411, 334
azul, verde, vermelho = imagem[v, u]
print('Pixel completo :', imagem[v, u])
print('Azul, verde, vermelho:', azul, verde, vermelho)
print('Só o vermelho  :', imagem[v, u, 2])

# um pixel da parede, para comparar
print('Pixel da parede:', imagem[120, 450])
