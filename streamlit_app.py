import streamlit as st

placeholder = st.empty()

with placeholder.container():
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  interp = st.text_input("What is the relationship between these two people? Who are they to each other?")
  clicked = st.button("submit")
  if clicked:
    st.write(interpretation)
    placeholder.empty()
  
  
