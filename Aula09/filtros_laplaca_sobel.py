#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

imagem = cv2.imread('../images/coins.jpg', 0)
imagem = cv2.medianBlur(imagem, 7)

laplace = cv2.Laplacian(imagem, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))

cv2.imshow('Imagem original', imagem)
cv2.imshow("Laplace", laplace)

sobelX = cv2.Sobel(imagem, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(imagem, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_combinado = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel combinado", sobel_combinado)

cv2.waitKey(0)