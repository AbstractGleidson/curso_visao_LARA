import cv2

captura = cv2.VideoCapture(0)          # 0 = primeira câmera do computador

while True:
    ret, quadro = captura.read()
    if not ret:
        break
    cv2.imshow('Webcam', quadro)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
