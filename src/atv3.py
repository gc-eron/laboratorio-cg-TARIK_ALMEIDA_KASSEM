import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Padrão")
k = st.slider("k", 1, 20, 4)
y, x = np.indices((64, 64))

def padrao(x, y, k):
    # Combinação própria: quadrados em x e y com um termo de interação.
    return ((x**2 + y**2 + x*y) * k) % 256

imagem = padrao(x, y, k).astype(np.uint8)
st.image(ampliar(imagem, 4), caption=f"Padrão de 64x64 pixels com k = {k}")
st.code("((x**2 + y**2 + x*y) * k) % 256", language="python")
st.write("x indica a coluna e y indica a linha. O controle k altera o padrão. "
         "O resto da divisão por 256 mantém os tons entre 0 e 255.")
