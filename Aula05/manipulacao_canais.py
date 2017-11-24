#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

#Lendo imagens
imagem_original = cv2.imread('../images/lena.png',1)

#Separa os canais da imagem
(B, G, R) = cv2.split(imagem_original)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.imshow("Original", imagem_original)
cv2.waitKey(0)

#Juntando os canais
fusao = cv2.merge([B,G,R])
cv2.imshow("Imagem fundida", fusao)
cv2.waitKey(0)