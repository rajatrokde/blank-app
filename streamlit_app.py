import streamlit as st

st.title("Hello Streamlit 🌈")
st.write("This app is running on Streamlit Community Cloud!")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")
