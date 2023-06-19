import streamlit as st

clicked = st.button("submit")
while not clicked:
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  st.text_input("What is the relationship between these two people? Who are they to each other?")
st.write('new section')
