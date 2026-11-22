import cv2

AREA_MINIMA = 400


def mascara_vermelho(img, s_min=120, v_min=50):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.bitwise_or(cv2.inRange(hsv, (0, s_min, v_min), (10, 255, 255)),
                          cv2.inRange(hsv, (170, s_min, v_min), (179, 255, 255)))


def limpar_mascara(mascara, abrir=5, fechar=15):
    ee_abrir = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (abrir, abrir))
    ee_fechar = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (fechar, fechar))
    m = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, ee_abrir)
    return cv2.morphologyEx(m, cv2.MORPH_CLOSE, ee_fechar)


def encontrar_bola(img):
    """Devolve (u, v, h, area) do maior contorno vermelho, ou None."""
    suave = cv2.GaussianBlur(img, (5, 5), 0)
    mascara = limpar_mascara(mascara_vermelho(suave))
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos:
        return None
    maior = max(contornos, key=cv2.contourArea)
    area = cv2.contourArea(maior)
    if area < AREA_MINIMA:
        return None
    x, y, w, h = cv2.boundingRect(maior)
    return x + w // 2, y + h // 2, h, area


if __name__ == '__main__':
    for nome in ['foto1', 'foto2', 'foto5', 'foto8', 'foto9']:
        resultado = encontrar_bola(cv2.imread(f'imagens/{nome}.jpg'))
        if resultado is None:
            print(nome, '-> sem bola')
        else:
            u, v, h, area = resultado
            print(f'{nome} -> u = {u:3d} | v = {v:3d} | h = {h:3d} | área = {area:7.0f}')
