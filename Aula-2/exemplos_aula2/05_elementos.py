import cv2

for nome, forma in [('MORPH_RECT', cv2.MORPH_RECT), ('MORPH_ELLIPSE', cv2.MORPH_ELLIPSE),
                    ('MORPH_CROSS', cv2.MORPH_CROSS)]:
    elemento = cv2.getStructuringElement(forma, (5, 5))
    print(nome)
    print(elemento)
