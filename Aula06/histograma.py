#Importando biblioteca do OpenCV
import cv2
#Importando biblioteca de visualização de gráficos
from matplotlib import pyplot as plt

imagem = cv2.imread('../images/shark.jpg', 0)

cv2.imshow("Cenario", imagem)

#Calculando histograma
hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histograma - Escala de Cinza")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)