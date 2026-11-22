import cv2

imagem = cv2.imread('imagens/foto9.jpg')
suave = cv2.GaussianBlur(imagem, (5, 5), 0)
hsv = cv2.cvtColor(suave, cv2.COLOR_BGR2HSV)
mascara = cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                         cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))

ee_abrir = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
ee_fechar = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

aberta = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, ee_abrir)
fechada = cv2.morphologyEx(aberta, cv2.MORPH_CLOSE, ee_fechar)
erodida = cv2.erode(mascara, ee_abrir, iterations=3)
dilatada = cv2.dilate(mascara, ee_abrir, iterations=3)

for nome, m in [('crua', mascara), ('erodida (3x)', erodida), ('dilatada (3x)', dilatada),
                ('aberta', aberta), ('aberta e fechada', fechada)]:
    n, _ = cv2.connectedComponents(m)
    print(f'{nome:17s}: {n - 1} regiões, {cv2.countNonZero(m):6d} pixels brancos')

cv2.imshow('Mascara crua', mascara)
cv2.imshow('Erodida', erodida)
cv2.imshow('Dilatada', dilatada)
cv2.imshow('Aberta e fechada', fechada)
cv2.waitKey(0)
cv2.destroyAllWindows()
