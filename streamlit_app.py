import streamlit as st

placeholder = st.empty()

with placeholder.container():
  st.image("https://i.imgur.com/VeuZ9cG.gif", width=700)
  form = st.form(key='my_form')
  interp = form.text_input(label="What is the relationship between these two people? Who are they to each other?")
  submit_button = form.form_submit_button(label='Submit')
  if submit_button:
    interpretation = interp
    placeholder.empty()
st.write(interpretation)
st.write(interp)
  #interp = st.text_input("What is the relationship between these two people? Who are they to each other?")
  #clicked = st.button("submit")
  #if clicked:
  #  st.write(interpretation)
  #  placeholder.empty()
  
  
