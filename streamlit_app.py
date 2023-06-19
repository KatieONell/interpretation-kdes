import streamlit as st

placeholder1 = st.empty()
placeholder2 = st.empty()

placeholder1.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
placeholder2.text_input("What is the relationship between these two people? Who are they to each other?")
clicked = st.button("submit")
if clicked:
  interpretation = placeholder2
  placeholder1.empty()
  placeholder2.empty()
  st.write(interpretation)
  
  
