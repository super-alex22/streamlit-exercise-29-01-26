import streamlit as st
st.write("Do you like python?")
answer = st.radio("Do you love python", ("yes", "no"))
if answer == "yes":
  st.write("Spectacular! Keep it up")
else:
  st.write("You dont seem to have a choice")
