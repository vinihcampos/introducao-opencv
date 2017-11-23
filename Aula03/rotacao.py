#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
imagem = cv2.imread('../images/lena.png')

#Obtendo as dimensões da imagem
h, w, _ = imagem.shape

#Definindo o centro da imagem
centro_imagem = (w / 2, h / 2)

#Angulo de rotacao
angulo = 90

#Definindo centro de rotação
centro_rotacao = cv2.getRotationMatrix2D(centro_imagem, angulo, 1.0)

cv2.imshow('Imagem original', imagem)
cv2.waitKey(0)

imagem = cv2.warpAffine(imagem, centro_rotacao, (w,h))

cv2.imshow('Imagem com rotação de 90 graus', imagem)
cv2.waitKey(0)