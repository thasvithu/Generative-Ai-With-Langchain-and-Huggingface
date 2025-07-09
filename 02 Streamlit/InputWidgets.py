import streamlit as st

def input_widgets():
    st.title("Input Widgets Example")
    
    # Text input
    name = st.text_input("Enter your name:")
    st.write(f"Hello, {name}!")
    
    # Number input
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
    st.write(f"You are {age} years old.")
    
    # Slider
    rating = st.slider("Rate your experience (1-10):", 1, 10, 5)
    st.write(f"You rated your experience as {rating}.")
    
    # Checkbox
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.write("Thank you for agreeing!")
    
    # Radio buttons
    option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")
    
    # Selectbox
    fruit = st.selectbox("Select a fruit:", ["Apple", "Banana", "Cherry"])
    st.write(f"You selected: {fruit}")