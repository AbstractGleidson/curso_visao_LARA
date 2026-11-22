import cv2

captura = cv2.VideoCapture('videos/video2.mp4')
if not captura.isOpened():
    raise RuntimeError('não consegui abrir o vídeo')

print('Quadros por segundo:', captura.get(cv2.CAP_PROP_FPS))
print('Total de quadros   :', int(captura.get(cv2.CAP_PROP_FRAME_COUNT)))
print('Largura x altura   :', int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)),
      'x', int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)))

lidos = 0
while True:
    ret, quadro = captura.read()
    if not ret:
        break
    lidos += 1
captura.release()
print('Quadros lidos      :', lidos)
