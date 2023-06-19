from sentence_transformers import SentenceTransformer
import pickle as pl

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

@st.cache_resource
def get_model():
  return SentenceTransformer('all-mpnet-base-v2')

@st.cache_data
def get_transform():
  return np.load("transform.npy", allow_pickle=True)

@st.cache_data
def get_mean_sub():
  return np.load("mean_sub.npy", allow_pickle=True)
  
placeholder = st.empty()

showMap = False
with placeholder.container():
  st.image("https://i.imgur.com/FpTf3hb.gif", width=700)
  form = st.form(key='my_form')
  interp = form.text_input(label="What is the relationship between these two people? Who are they to each other?", key='samplekey')
  embedding = ''
  submit_button = form.form_submit_button(label='Submit')
  if submit_button:
    placeholder.empty()
    showMap = True

if showMap:
  embedding = get_model().encode([interp])
  input = embedding - get_mean_sub()
  your_point = np.matmul(input, get_transform())

  st.title(interp)
  fig_handle = pl.load(open('kde.pickle','rb'))
  ax = fig_handle.get_axes()
  #fig_handle.title(interp)
  ax[0].vlines(x=your_point[:,0], ymin=your_point[:,1], ymax=your_point[:,1]+0.085, color='k')
  ax[0].scatter(your_point[:,0], your_point[:,1]+0.1, color='k', s=100)
  ax[0].scatter(your_point[:,0], your_point[:,1]+0.1, color='tab:red', s=50)
  #ax[0].set_title("\""+interp+"\"", fontsize=30)
  st.pyplot(fig_handle)



  
