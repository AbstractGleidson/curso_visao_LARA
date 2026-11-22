import cv2

imagem = cv2.imread('imagens/foto4.jpg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

verdes = cv2.inRange(hsv, (35, 120, 40), (85, 255, 255))
verde_clara = cv2.inRange(hsv, (35, 120, 40), (55, 255, 255))
verde_escura = cv2.inRange(hsv, (56, 120, 40), (85, 255, 255))

for nome, m in [('as duas', verdes), ('verde clara', verde_clara), ('verde escura', verde_escura)]:
    print(f'{nome:12s}: {cv2.countNonZero(m):6d} pixels')

cv2.imshow('Verdes (H 35 a 85)', verdes)
cv2.imshow('Verde clara (H 35 a 55)', verde_clara)
cv2.imshow('Verde escura (H 56 a 85)', verde_escura)
cv2.waitKey(0)
cv2.destroyAllWindows()
