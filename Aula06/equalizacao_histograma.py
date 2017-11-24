#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca de visualização de gráficos
import numpy as np

imagem = cv2.imread('../images/retina.jpg', 0)

#Redimensionando pois a imagem é muito grande
h, w = imagem.shape
imagem = cv2.resize(imagem, (400,400), (w,h))

imagem_equalizada = cv2.equalizeHist(imagem)

cv2.imshow('Retina', imagem)
cv2.imshow('Retina equalizada', imagem_equalizada)
cv2.waitKey(0)

