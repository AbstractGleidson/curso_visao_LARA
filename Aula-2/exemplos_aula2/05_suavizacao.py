import cv2

def mascara_vermelho(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.bitwise_or(cv2.inRange(hsv, (0, 120, 50), (10, 255, 255)),
                          cv2.inRange(hsv, (170, 120, 50), (179, 255, 255)))

def regioes(mascara):
    n, _ = cv2.connectedComponents(mascara)
    return n - 1                         # o rótulo 0 é o fundo

imagem = cv2.imread('imagens/foto5.jpg')
versoes = {
    'sem filtro        ': imagem,
    'blur (média 5x5)  ': cv2.blur(imagem, (5, 5)),
    'GaussianBlur 5x5  ': cv2.GaussianBlur(imagem, (5, 5), 0),
    'medianBlur 5      ': cv2.medianBlur(imagem, 5),
}
for nome, img in versoes.items():
    print(nome, '-> regiões na máscara:', regioes(mascara_vermelho(img)))
