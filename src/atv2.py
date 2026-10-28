import numpy as np
import streamlit as st

def ampliar(imagem, k=10):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira de Gana")
# Proporção 2:3; três faixas horizontais de mesma altura.
bandeira = np.zeros((60, 90, 3), dtype=np.uint8)
bandeira[:20, :] = (206, 17, 38)     # vermelho
bandeira[20:40, :] = (252, 209, 22)  # amarelo
bandeira[40:, :] = (0, 107, 63)     # verde

# Estrela preta de cinco pontas, desenhada por uma máscara de pixels.
y, x = np.indices((60, 90))
mascara = np.zeros((60, 90), dtype=bool)
angulos = np.arange(10) * np.pi / 5 - np.pi / 2
raios = np.where(np.arange(10) % 2 == 0, 10, 3.82)
vx = 44.5 + raios * np.cos(angulos)
vy = 30 + raios * np.sin(angulos)
for i in range(10):
    j = (i + 1) % 10
    cruza = (vy[i] > y) != (vy[j] > y)
    limite = (vx[j] - vx[i]) * (y - vy[i]) / (vy[j] - vy[i]) + vx[i]
    mascara ^= cruza & (x < limite)
bandeira[mascara] = (0, 0, 0)

st.image(ampliar(bandeira), caption="Bandeira de Gana em pixels")
st.write("Formato:", bandeira.shape)
st.write("Cores RGB: vermelho (206, 17, 38), amarelo (252, 209, 22), "
         "verde (0, 107, 63) e preto (0, 0, 0).")
