from sentence_transformers import SentenceTransformer

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

@st.cache_resource
def get_model():
  return SentenceTransformer('all-mpnet-base-v2')

  
placeholder = st.empty()

with placeholder.container():
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  form = st.form(key='my_form')
  interp = form.text_input(label="What is the relationship between these two people? Who are they to each other?", key='samplekey')
  embedding = ''
  submit_button = form.form_submit_button(label='Submit')
  if submit_button:
    placeholder.empty()
    embedding = get_model().encode([interp])
  st.write(interp)
  st.write(str(embedding))



  
