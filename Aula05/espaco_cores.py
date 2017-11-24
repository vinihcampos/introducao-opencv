#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

#Lendo imagens
imagem_original = cv2.imread('../images/dory.jpg')

cv2.imshow("Original", imagem_original)

#Escala de cinza
cv2.imshow("Escala de cinza", cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY))

#Este espaço de cor é mais similiar com a forma como os humanos pensam e concebem a cor.
cv2.imshow("HSV", cv2.cvtColor(imagem_original, cv2.COLOR_BGR2HSV))

#Este, está mais ajustado a forma que os humanos percebem as cores.
cv2.imshow("L*a*b*", cv2.cvtColor(imagem_original, cv2.COLOR_BGR2LAB))
cv2.waitKey(0)