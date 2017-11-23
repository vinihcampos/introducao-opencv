#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca para computação científica
import numpy as np

#Lendo imagens
imagem_original = cv2.imread('../images/shark.jpg')

#Matriz para realizações as operações
m = np.ones(imagem_original.shape, dtype = "uint8") * 100

imagem_adicionada = cv2.add(imagem_original, m)
imagem_subtraida = cv2.subtract(imagem_original, m)

cv2.imshow('Imagem original', imagem_original)
cv2.waitKey(0)

cv2.imshow('Imagem com todos os pixels adicionados em 100', imagem_adicionada)
cv2.waitKey(0)

cv2.imshow('Imagem com todos os pixels subtraidos em 100', imagem_subtraida)
cv2.waitKey(0)

medias = cv2.mean(imagem_original)
media = round((medias[0] + medias[1] + medias[2]) / 3)

m = np.ones(imagem_original.shape, dtype = "uint8") * media

imagem_adicionada = cv2.add(imagem_original, m)
imagem_subtraida = cv2.subtract(imagem_original, m)

cv2.imshow('Imagem com todos os pixels adicionando a média', imagem_adicionada)
cv2.waitKey(0)

cv2.imshow('Imagem com todos os pixels subtraindo a média', imagem_subtraida)
cv2.waitKey(0)

print (medias)
