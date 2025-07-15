
import streamlit as st

st.header('st.button("Nome do botão")') # cria um cabeçalho

if st.button('Botão'):
    st.write('Botão clicado!')
else: 
    st.write('Botao não clicado...')