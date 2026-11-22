import cv2

imagem = cv2.imread('imagens/foto2.jpg')
hsv = cv2.cvtColor(cv2.GaussianBlur(imagem, (5, 5), 0), cv2.COLOR_BGR2HSV)
mascara = cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                         cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))

contornos, hierarquia = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Contornos encontrados:', len(contornos))

areas = sorted((cv2.contourArea(c) for c in contornos), reverse=True)
print('As cinco maiores áreas:', [round(a) for a in areas[:5]])
print('Pontos do primeiro contorno:', contornos[0].shape)

desenho = imagem.copy()
cv2.drawContours(desenho, contornos, -1, (0, 255, 255), 2)
cv2.imshow('Contornos', desenho)
cv2.waitKey(0)
cv2.destroyAllWindows()
