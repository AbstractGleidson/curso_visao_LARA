import cv2
from encontrar_bola import encontrar_bola

KP_GIRO = 1 / 320
KP_AVANCO = 1 / 150
H_DESEJADO = 150


def saturar(valor, limite=1.0):
    return max(-limite, min(limite, valor))


for nome in ['foto2', 'foto5', 'foto8', 'foto9']:
    imagem = cv2.imread(f'imagens/{nome}.jpg')
    cx = imagem.shape[1] // 2
    u, v, h, area = encontrar_bola(imagem)
    erro_u = cx - u
    erro_h = H_DESEJADO - h
    omega = saturar(KP_GIRO * erro_u)
    velocidade = saturar(KP_AVANCO * erro_h)
    print(f'{nome}: e_u = {erro_u:+4d} | e_h = {erro_h:+4d} | '
          f'omega = {omega:+.2f} | v = {velocidade:+.2f}')
