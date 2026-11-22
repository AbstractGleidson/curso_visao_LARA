import cv2

imagem = cv2.imread('imagens/foto4.jpg')

cv2.imshow('Rover', imagem)
tecla = cv2.waitKey(0)          # espera uma tecla; 0 = para sempre
cv2.destroyAllWindows()
print('Código da tecla pressionada:', tecla)
