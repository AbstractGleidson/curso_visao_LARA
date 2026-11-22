import cv2

imagem = cv2.imread('imagens/foto2.jpg')
hsv = cv2.cvtColor(cv2.GaussianBlur(imagem, (5, 5), 0), cv2.COLOR_BGR2HSV)
mascara = cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                         cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))
ee_abrir = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
ee_fechar = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, ee_abrir)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, ee_fechar)

contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
maior = max(contornos, key=cv2.contourArea)

x, y, w, h = cv2.boundingRect(maior)
momentos = cv2.moments(maior)
u = momentos['m10'] / momentos['m00']
v = momentos['m01'] / momentos['m00']

print('Área do contorno     :', cv2.contourArea(maior))
print('Caixa envolvente     : x =', x, 'y =', y, 'w =', w, 'h =', h)
print('Centro da caixa      :', (x + w // 2, y + h // 2))
print('Centroide (momentos) :', (round(u, 1), round(v, 1)))

desenho = imagem.copy()
cv2.rectangle(desenho, (x, y), (x + w, y + h), (255, 200, 0), 3)
cv2.drawMarker(desenho, (round(u), round(v)), (255, 255, 0), cv2.MARKER_CROSS, 30, 3)
cv2.imshow('Maior contorno', desenho)
cv2.waitKey(0)
cv2.destroyAllWindows()
