#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

image = cv2.imread('../images/coins.jpg')
imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imagem = cv2.medianBlur(imagem, 5)
#imagem = cv2.equalizeHist(imagem)

#Detectando as bordas
canny = cv2.Canny(imagem, 30, 150)
cv2.imshow("Original", imagem)
cv2.imshow("Canny", canny)

_,objects,_ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print ("I count %d coins in this image" % (len(objects)))

cv2.drawContours(image, objects, -1, (0, 255, 0), 2)
cv2.imshow("Moedas", image)
cv2.waitKey(0)

cv2.waitKey(0)