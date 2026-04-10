import streamlit as st

st.title("My Python App")

st.write("Hello Python 👋")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}!")