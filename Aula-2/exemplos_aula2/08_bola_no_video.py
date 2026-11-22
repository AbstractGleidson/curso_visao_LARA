import time
import cv2
from encontrar_bola import encontrar_bola

captura = cv2.VideoCapture('videos/video4.mp4')
tempos, com_bola, quadros = [], 0, 0

while True:
    ret, quadro = captura.read()
    if not ret:
        break
    inicio = time.perf_counter()
    resultado = encontrar_bola(quadro)
    tempos.append(1000 * (time.perf_counter() - inicio))
    quadros += 1
    if resultado is not None:
        com_bola += 1
        if quadros % 150 == 1:
            u, v, h, area = resultado
            print(f'quadro {quadros:3d}: u = {u}, h = {h}')

captura.release()
print(f'Bola encontrada em {com_bola} de {quadros} quadros ({100 * com_bola / quadros:.0f}%)')
print(f'Tempo médio por quadro: {sum(tempos) / len(tempos):.1f} ms (orçamento: 33 ms)')
