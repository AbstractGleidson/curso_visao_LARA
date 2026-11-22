import cv2

imagem = cv2.imread('imagens/foto5.jpg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
mascara = cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                         cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))

# mantém a cor original só onde a máscara é branca
somente_vermelho = cv2.bitwise_and(imagem, imagem, mask=mascara)

cv2.imshow('Original', imagem)
cv2.imshow('Mascara', mascara)
cv2.imshow('Somente vermelho', somente_vermelho)
cv2.waitKey(0)
cv2.destroyAllWindows()
