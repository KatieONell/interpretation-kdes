from sentence_transformers import SentenceTransformer
import pickle as pl

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

@st.cache_resource
def get_model():
  return SentenceTransformer('all-mpnet-base-v2')

def get_transform():
  return np.load("transform.npy", allow_pickle=True)
  
placeholder = st.empty()

showMap = False
with placeholder.container():
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  form = st.form(key='my_form')
  interp = form.text_input(label="What is the relationship between these two people? Who are they to each other?", key='samplekey')
  embedding = ''
  submit_button = form.form_submit_button(label='Submit')
  if submit_button:
    placeholder.empty()
    showMap = True

if showMap:
  embedding = get_model().encode([interp])
  input = embedding - embedding.mean(axis=0, keepdims=True)
  your_point = np.matmul(input, get_transform())

  
  fig_handle = pl.load(open('kde.pickle','rb'))
  fig_handle.title(interp)
  fig_handle.scatter(your_point[:,0], your_point[:,1])
  st.pyplot(fig_handle)



  
