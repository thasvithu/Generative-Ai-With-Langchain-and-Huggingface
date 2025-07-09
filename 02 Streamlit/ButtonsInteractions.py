import streamlit as st

def buttons_interactions():
    st.title("Buttons and Interactions Example")
    
    # Button
    if st.button("Click Me"):
        st.write("Button clicked!")
    
    # Button with a callback
    def button_callback():
        st.write("Button with callback clicked!")
    
    if st.button("Click Me with Callback", on_click=button_callback):
        pass
    
    # Multiple buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Button 1"):
            st.write("Button 1 clicked!")
    
    with col2:
        if st.button("Button 2"):
            st.write("Button 2 clicked!")