# Importando biblioteca do OpenCV
import cv2

# Lendo imagemns
imagem = cv2.imread('../images/dory.jpg')

print(imagem.shape)

# Obtendo as dimensões da imagemm
row,col,_ = imagem.shape

# Mostrando o valor do pixel na posição 0, 0
(b, g, r) = imagem[0, 0]
print ("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

cv2.imshow('imagemm original', imagem)
cv2.waitKey(0)

imagem_original = imagem.copy();

# Alterando os valors dos pixels de um quarto da imagemm
for i in range (round(row/2)):
	for j in range (round(col/2)):
		imagem[i, j] = (255, 0, 0)

cv2.imshow('imagem pintada', imagem)
cv2.waitKey(0)

cv2.imshow('imagem original', imagem_original)
cv2.waitKey(0)

# Além dessa forma, temos:
imagem = imagem_original.copy()
imagem[0:round(row/2), 0:round(col/2) ] = (255, 0, 0)

cv2.imshow('imagem pintada', imagem)
cv2.waitKey(0)

#Desenhando um círculo
imagem = imagem_original.copy()

centroX = round(col/2)
centroY = round(row/2)

cv2.circle(imagem, (centroX, centroY), centroY, (0, 255, 0) )
cv2.imshow('imagem pintada', imagem)
cv2.waitKey(0)
