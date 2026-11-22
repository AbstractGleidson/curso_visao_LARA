import cv2

imagem = cv2.imread('imagens/foto4.jpg')
desenho = imagem.copy()                 # desenhe sempre numa cópia

altura, largura = desenho.shape[:2]
cx = largura // 2
cv2.line(desenho, (cx, 0), (cx, altura - 1), (255, 255, 255), 1)
cv2.rectangle(desenho, (350, 270), (475, 400), (255, 200, 0), 3)
cv2.circle(desenho, (150, 398), 77, (0, 255, 255), 3)
cv2.drawMarker(desenho, (411, 334), (255, 255, 0), cv2.MARKER_CROSS, 30, 3)
cv2.putText(desenho, 'u = 411', (360, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv2.imwrite('saida_desenho.png', desenho)
cv2.imshow('Desenho', desenho)
cv2.waitKey(0)
cv2.destroyAllWindows()
