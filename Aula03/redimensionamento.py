#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
imagem_original = cv2.imread('../images/lena.png')

#Obtendo as dimensões da imagem
h, w, _ = imagem_original.shape

#Escala em %
escala = 50.0

cv2.imshow('Imagem original', imagem_original)
cv2.waitKey(0)

metade = cv2.resize(imagem_original, (round(escala / 100.0 * w), round(escala / 100.0 * h)), (w,h))

cv2.imshow('Imagem com metade do tamanho original', metade)
cv2.waitKey(0)

# Redefinindo a escala
escala = 200.0

dobro = cv2.resize(imagem_original, (round(escala / 100.0 * w), round(escala / 100.0 * h)), (w,h))

cv2.imshow('Imagem com o dobro do tamanho original', dobro)
cv2.waitKey(0)