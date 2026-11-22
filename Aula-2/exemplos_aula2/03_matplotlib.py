import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('imagens/foto4.jpg')
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
mascara = cv2.inRange(hsv, (170, 120, 50), (179, 255, 255))

fig, eixos = plt.subplots(1, 4, figsize=(14, 4))
eixos[0].imshow(imagem)                                    # errado: BGR
eixos[0].set_title('BGR mostrado direto')
eixos[1].imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))   # certo: RGB
eixos[1].set_title('convertido para RGB')
eixos[2].imshow(mascara)                                   # mapa de cores padrão
eixos[2].set_title('máscara sem cmap')
eixos[3].imshow(mascara, cmap='gray', vmin=0, vmax=255)    # tons de cinza
eixos[3].set_title("cmap='gray', vmin=0, vmax=255")
for eixo in eixos:
    eixo.axis('off')
plt.tight_layout()
plt.show()
