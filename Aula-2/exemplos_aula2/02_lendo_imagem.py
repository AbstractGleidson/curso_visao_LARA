import cv2

imagem = cv2.imread('imagens/foto4.jpg')

if imagem is None:
    print('Imagem não encontrada: confira o caminho')
else:
    print('Tipo do objeto:', type(imagem))
    print('Dimensões     :', imagem.shape)
    print('Tipo dos dados:', imagem.dtype)
    print('Total de números:', imagem.size)
