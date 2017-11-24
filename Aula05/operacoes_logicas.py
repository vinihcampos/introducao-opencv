#Importando biblioteca do OpenCV
import cv2

#Lendo imagens
quebra_cabeca = cv2.imread('../images/puzzle.jpg')
parte1 = cv2.imread('../images/puzzle_part1.jpg')
parte2 = cv2.imread('../images/puzzle_part2.jpg')

#Mostrando imagens
cv2.imshow('Puzzle completo', quebra_cabeca)
cv2.waitKey(0)

#Mostrando imagens
cv2.imshow('Puzzle parte 1', parte1)
cv2.waitKey(0)

cv2.imshow('Puzzle parte 2', parte2)
cv2.waitKey(0)

#Aplicando operações lógicas
cv2.imshow("AND", cv2.bitwise_and(parte1, quebra_cabeca))
cv2.waitKey(0)

cv2.imshow("OR", cv2.bitwise_or(parte1, parte2))
cv2.waitKey(0)

cv2.imshow("XOR", cv2.bitwise_xor(parte1, parte2))
cv2.waitKey(0)

cv2.imshow("NOT", cv2.bitwise_not(quebra_cabeca))
cv2.waitKey(0)
