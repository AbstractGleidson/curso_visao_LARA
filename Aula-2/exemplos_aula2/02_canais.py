import cv2

imagem = cv2.imread('imagens/foto4.jpg')
azul, verde, vermelho = cv2.split(imagem)

print('Dimensões de cada canal:', vermelho.shape)

cv2.imshow('Canal azul', azul)
cv2.imshow('Canal verde', verde)
cv2.imshow('Canal vermelho', vermelho)
cv2.waitKey(0)
cv2.destroyAllWindows()
