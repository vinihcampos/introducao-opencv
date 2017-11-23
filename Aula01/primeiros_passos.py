#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
img = cv2.imread('../images/lena.png')

#Mostrando imagens
cv2.imshow('Exemplo', img)

#É preciso informar que o programa deve esperar alguma tecla ser pressionada
cv2.waitKey(0)

#Salvando a imagem mostrada
cv2.imwrite('../images/lena_salva.png', img)