#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

imagem = cv2.imread('../images/coins.jpg', 0)
imagem = cv2.medianBlur(imagem, 5)

#Detectando as bordas
canny = cv2.Canny(imagem, 30, 150)
cv2.imshow("Original", imagem)
cv2.imshow("Canny", canny)
cv2.waitKey(0)