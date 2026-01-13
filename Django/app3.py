#calculator app
import streamlit as st
st.title("Calculator App")
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operator = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])


if st.button("Calculate"):
    if operator == "Add":
        result = num1 + num2
    elif operator == "Subtract":
        result = num1 - num2
    elif operator == "Multiply":
        result = num1 * num2
    elif operator == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.write(f"The result is: {result}")