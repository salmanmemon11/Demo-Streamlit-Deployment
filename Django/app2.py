import streamlit as st

st.title("some basic commands like slider, button, etc.")

age = st.slider("How old are you?", 1,100)

city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Bangalore", "Chennai","Pune"])
if st.button("Show details"):
    st.write(f"You are {age} years old and you live in {city}.")
st.write("Thank you for using the app!")


