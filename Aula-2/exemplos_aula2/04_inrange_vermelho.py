import cv2
import numpy as np

imagem = cv2.imread('imagens/foto2.jpg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

tom_baixo_1, tom_alto_1 = np.array([0, 120, 50]), np.array([10, 255, 255])
tom_baixo_2, tom_alto_2 = np.array([170, 120, 50]), np.array([179, 255, 255])

ponta_baixa = cv2.inRange(hsv, tom_baixo_1, tom_alto_1)
ponta_alta = cv2.inRange(hsv, tom_baixo_2, tom_alto_2)
mascara = cv2.bitwise_or(ponta_baixa, ponta_alta)

print('Tipo e forma da máscara:', mascara.dtype, mascara.shape)
print('Valores na máscara     :', np.unique(mascara))
print('Pixels brancos: H 0-10 =', cv2.countNonZero(ponta_baixa),
      '| H 170-179 =', cv2.countNonZero(ponta_alta),
      '| juntas =', cv2.countNonZero(mascara))

cv2.imshow('H 0 a 10', ponta_baixa)
cv2.imshow('H 170 a 179', ponta_alta)
cv2.imshow('Duas faixas', mascara)
cv2.waitKey(0)
cv2.destroyAllWindows()
