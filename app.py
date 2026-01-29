import streamlit as st
st.write("Do you like python?")
answer = st.radio("Do you love python", ("yes", "no"))
if answer == "yes":
  st.write("Spectacular! Keep it up")
else:
  st.write("You dont seem to have a choice")
st.write("I'd like to humbly ask your Mightiness to enter number")
number = st.number_input("Have the number entered in this field")
if(number>10):
  st.write("The number is enormous")
else:
  st.write("The number is miserable")
