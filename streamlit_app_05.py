# varias formas de dar print na tela 
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write') # cabecalho com texto "st.write"

# Example 1
st.write('Esse é um texto de exemplo usando <st.write>')

# Example 2
st.write(1234) # texto com numeros 

# Example 3 - Exemplo usando dataframe  
df = pd.DataFrame({
    'first column'  : [1,2,3,4],
    'second column' : [10,20,30,40]
    })
st.write(df)

# Example 4 -
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5 -
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

