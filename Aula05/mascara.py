#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
quebra_cabeca = cv2.imread('../images/puzzle.jpg')
mascara = cv2.imread('../images/puzzle_mascara.jpg', 0) #lê a imagem automaticamente na escala de cinza

#Mostrando imagens
cv2.imshow('Puzzle completo', quebra_cabeca)
cv2.waitKey(0)

cv2.imshow('Mascara', mascara)
cv2.waitKey(0)

#Aplicando a mascara no puzzle
cv2.imshow("Imagem mascarada", cv2.bitwise_and(quebra_cabeca, quebra_cabeca, mask = mascara))
cv2.waitKey(0)
