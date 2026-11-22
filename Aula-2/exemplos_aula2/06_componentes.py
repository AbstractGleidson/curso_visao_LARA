import cv2

imagem = cv2.imread('imagens/foto2.jpg')
hsv = cv2.cvtColor(cv2.GaussianBlur(imagem, (5, 5), 0), cv2.COLOR_BGR2HSV)
mascara = cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                         cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))
ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, ee)

n, rotulos, stats, centros = cv2.connectedComponentsWithStats(mascara)

print('Número de rótulos (com o fundo):', n)
print('rótulo |   x    y    w    h |  área | centroide')
for i in range(n):
    x, y, w, h, area = stats[i]
    cu, cv = centros[i]
    print(f'{i:6d} | {x:3d}  {y:3d}  {w:3d}  {h:3d} | {area:6d} | ({cu:5.1f}, {cv:5.1f})')
