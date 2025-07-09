import streamlit as st

def forms_example():
    st.title("Forms Example")

    # Create a form
    with st.form(key='my_form'):
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f"Hello, {name}! You are {age} years old.")
    
    # Another form for feedback
    with st.form(key='feedback_form'):
        feedback = st.text_area("Your feedback:")
        feedback_submit = st.form_submit_button(label='Submit Feedback')

    if feedback_submit:
        st.write("Thank you for your feedback!")