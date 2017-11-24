#Importando biblioteca do OpenCV
import cv2

imagem = cv2.imread('../images/coins.jpg', 0)
h,w = imagem.shape
#imagem = cv2.resize(imagem, (round(.5 * w), round(.5 * h)), (w,h))

cv2.imshow('Imagem original', imagem)

#Aplicando binarização simples
_, binarizacao = cv2.threshold(imagem, 155, 255, cv2.THRESH_BINARY)
#Aplicando binarização invertida
_, binarizacao_inv = cv2.threshold(imagem, 155, 255, cv2.THRESH_BINARY_INV)
#Aplicando binarização invertida
_, binarizacao_otsu = cv2.threshold(imagem, 155, 255, cv2.THRESH_OTSU)

cv2.imshow("Binarizacao simples", binarizacao)
cv2.imshow("Binarizacao invertida", binarizacao_inv)
cv2.imshow("Binarizacao otsu", binarizacao_otsu)

binarizacao_otsu = cv2.bitwise_not(binarizacao_otsu)

cv2.imshow("Moedas apos binarizacao otsu", cv2.bitwise_and( imagem, imagem, mask = binarizacao_otsu ))

cv2.waitKey(0)