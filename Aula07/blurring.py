#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca de visualização de gráficos
import numpy as np

imagem = cv2.imread('../images/noise.png')

h,w,_ = imagem.shape

imagem = cv2.resize(imagem, (round(.25 * w), round(.25 * h)), (w,h))

#Aplicando filtro de média
media = np.hstack([cv2.blur(imagem, (3, 3)),cv2.blur(imagem, (5, 5)),cv2.blur(imagem, (7, 7))])
cv2.imshow("Filtro de media", media)

#Aplicando filtro gaussiano
gaussiano = np.hstack([cv2.GaussianBlur(imagem, (3, 3), 0),cv2.GaussianBlur(imagem, (5, 5), 0),cv2.GaussianBlur(imagem, (7, 7), 0)])
cv2.imshow("Filtro Gaussiano", gaussiano)

#Aplicando filtro de mediana
mediana = np.hstack([cv2.medianBlur(imagem, 3),cv2.medianBlur(imagem, 5),cv2.medianBlur(imagem, 7)])
cv2.imshow("Filtro de mediana", mediana)
cv2.waitKey(0)