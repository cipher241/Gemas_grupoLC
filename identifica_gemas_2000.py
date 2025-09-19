!pip install opencv-python

import cv2
import numpy as np
from matplotlib import pyplot as plt

print("---------Gemas disponibles-----------")
print("1 = Verde")
print("2 = Azul")
print("3 = Roja ")
print("4 = Amarilla")
print("5 = Naranja")
print("6 = Morada")
user_input = 1

img = cv2.imread("gemas1.jpeg")
assert img is not None, "file could not be read, check with os.path.exists()"

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(12, 5))

plt.subplot(1,2,1)
plt.title("HSV original")
plt.imshow(cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB))
plt.axis("off")
plt.show()

# Definir rango de amarillo en HSV
lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

# Crear máscara (para detectar amarillo)
masky = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

# Definir rango de verde en HSV
lower_green = np.array([35, 40, 40], dtype=np.uint8)
upper_green = np.array([85, 255, 255], dtype=np.uint8)

# Crear máscara (para detectar verde)
maskg = cv2.inRange(img_hsv, lower_green, upper_green)

# Definir rango de azul en HSV
lower_blue = np.array([100, 150, 0], dtype=np.uint8)
upper_blue = np.array([140, 255, 255], dtype=np.uint8)

# Crear máscara (para detectar azul)
maskb = cv2.inRange(img_hsv, lower_blue, upper_blue)

# Definir rango de morado en HSV
lower_purple = np.array([130, 50, 50], dtype=np.uint8)
upper_purple = np.array([160, 255, 255], dtype=np.uint8)

# Crear máscara (para detectar morado)
maskp = cv2.inRange(img_hsv, lower_purple, upper_purple)

# Definir rango de rojo en HSV
lower_red1 = np.array([0, 120, 70], dtype=np.uint8)
upper_red1 = np.array([10, 255, 255], dtype=np.uint8)

lower_red2 = np.array([170, 120, 70], dtype=np.uint8)
upper_red2 = np.array([180, 255, 255], dtype=np.uint8)

# Crear máscaras (para detectar rojo)
mask_red1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(img_hsv, lower_red2, upper_red2)

# Combinar ambas máscaras
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

mask_red1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(img_hsv, lower_red2, upper_red2)

# Combinar ambas máscaras
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

if user_input == 1:
  result_verde = cv2.bitwise_and(img_hsv, img_hsv, mask=maskg)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_verde, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Esmeraldas")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
elif user_input == 2:
  result_azul = cv2.bitwise_and(img_hsv, img_hsv, mask=maskb)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_azul, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Zafiros")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
elif user_input == 3:
  result_roja = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_red2)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_roja, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Rubís")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
elif user_input == 4:
  result_amarillo = cv2.bitwise_and(img_hsv, img_hsv, mask=masky)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_amarillo, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Topacio")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
elif user_input == 5:
  result_naranja = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_red2)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_naranja, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Gasper")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
elif user_input == 6:
  result_morado = cv2.bitwise_and(img_hsv, img_hsv, mask=maskp)
  img_gray_rgb = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
  final_result = cv2.addWeighted(img_gray_rgb, 1, result_morado, 1, 0)

  plt.figure(figsize=(15, 5))

  plt.subplot(1, 1, 1)
  plt.title("Amatistas")
  plt.imshow(final_result)
  plt.axis("off")
  plt.show()
else:
  print("Opcion no valida")
