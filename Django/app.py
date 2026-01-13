import streamlit as st

st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application.")

st.title("some basic commands in streamlit")
name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write(f"Hello, {name}!")

