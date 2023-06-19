#!pip install sentence_transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


placeholder = st.empty()

with placeholder.container():
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  form = st.form(key='my_form')
  interp = form.text_input(label="What is the relationship between these two people? Who are they to each other?")
  submit_button = form.form_submit_button(label='Submit')
  if submit_button:
    placeholder.empty()

#after submitting an interpretation
if submit_button:
  st.write(interp)
  
  @st.cache_resource
  def get_model():
    return SentenceTransformer('all-mpnet-base-v2')
  
  model = get_model()
  embeddings = model.encode([interp])
  st.write(str(embeddings))

  
