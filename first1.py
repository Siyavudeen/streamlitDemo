import streamlit as st
import numpy as np
import pandas as pd
st.title('This is my first Streamlit app')

st.header('Header tag')
st.subheader('Header tag')
st.text('this is my text area i can write losg text like paragraph tag')
st.markdown('''
# Header 1
## Header 2
### Header 3
this is my *third* line
- two
- three
# to pass emoji 😂😂😂😂😂😂 windows+. nekkiya madi
:sunglasses:<br>
:joy:
# unsafe_allow_html=true pass cheythal html tag work aakum
''',unsafe_allow_html=True)

st.latex('''
a^2+ b^2= c^2
''')
directors= pd.read_csv('bike_sharing.csv')
directors=directors.head(8)


mylist=[1,2,3,4,5,6,7,8,9,10]
arr= np.array(mylist)
dim= arr.reshape(2,5)

st.subheader('--------------------------------------')
st.write('''
'this is my first text',
# markdown okky ividem work aakum
## header 2
- jack
- rose
        ''' )
st.write(
    'this is my directors data',directors,
    'array',arr
    ,dim
)
st.write('directors distcription',directors.describe())