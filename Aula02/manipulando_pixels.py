# Importando biblioteca do OpenCV
import cv2

# Lendo imagens
image = cv2.imread('../images/lena.png')

print(image.shape)

# Obtendo as dimensões da imagem
row,col,_ = image.shape

# Mostrando o valor do pixel na posição 0, 0
(b, g, r) = image[0, 0]
print ("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))
		

cv2.imshow('Imagem original', image)
cv2.waitKey(0)

# Alterando os valors dos pixels de um quarto da imagem
for i in range (round(row/2)):
	for j in range (round(col/2)):
		image[i, j] = (255, 0, 0)

cv2.imshow('Imagem pintada', image)
cv2.waitKey(0)