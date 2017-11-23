#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
imagem_original = cv2.imread('../images/dory.jpg')

#Obtendo as dimensões da imagem
h, w, _ = imagem_original.shape

cv2.imshow('Imagem original', imagem_original)
cv2.waitKey(0)

#Espelhando horizontalmente
horizontal = cv2.flip(imagem_original, 1);

#Espelhando verticalmente
vertical = cv2.flip(imagem_original, 0);

#Espelhando horizontalmente e verticalmente
horizontal_vertical = cv2.flip(imagem_original, -1);

cv2.imshow('Imagem espelhada horizontalmente', horizontal)
cv2.waitKey(0)

cv2.imshow('Imagem espelhada verticalmente', vertical)
cv2.waitKey(0)

cv2.imshow('Imagem espelhada horizontalmente e verticalmente', horizontal_vertical)
cv2.waitKey(0)