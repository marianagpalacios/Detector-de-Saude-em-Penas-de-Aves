import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carrega imagem
img = cv2.imread("ave.jpg")

# Converte para RGB (OpenCV usa BGR por padrão)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Exibe imagens
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Cinza")
plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.show()

# Detectar bordas
edges = cv2.Laplacian(gray, cv2.CV_64F)
edges = cv2.convertScaleAbs(edges)

plt.imshow(edges, cmap="gray")
plt.title("Textura / Bordas")
plt.axis("off")
plt.show()

# Métrica de irregularidade
desvio_textura = np.std(edges)
print(f"Desvio padrão da textura: {desvio_textura:.2f}")
# Se o desvio padrão é muito alto → penas com manchas/irregularidades.
# Se for baixo → penas mais uniformes (saudáveis).

def classificar_penagem(desvio):
    if desvio < 20:
        return "Penas parecem saudáveis"
    elif desvio < 40:
        return "Penas possivelmente com pequenas irregularidades"
    else:
        return "Penas com sinais de problemas"

print(classificar_penagem(desvio_textura))
