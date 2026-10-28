import streamlit as st
import numpy as np

st.title("Computação Gráfica")
st.write("Meu nome é Tarik Almeida Kassem.")
n = st.slider("Tamanho", 2, 64, 8)
img = np.full((n, n), 128, dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)
