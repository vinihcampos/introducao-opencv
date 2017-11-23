#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
imagem_original = cv2.imread('../images/dory.jpg')

#Obtendo as dimensões da imagem
h, w, _ = imagem_original.shape

#Definindo os pontos de corte para formar retângulos
inicial_x = 0
final_x = round(w / 2)
inicial_y = 0
final_y = round(h / 2)

# Recortando um quarto da imagem
imagem_cortada = imagem_original[ inicial_y:final_y, inicial_x:final_x ]

cv2.imshow('Imagem original', imagem_original)
cv2.waitKey(0)

cv2.imshow('Imagem cortada', imagem_cortada)
cv2.waitKey(0)