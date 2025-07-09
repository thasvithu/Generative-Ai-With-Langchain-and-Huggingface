import streamlit as st

def display_elements():
    st.title("Display Elements Example")
    
    # Displaying text
    st.header("Header: Welcome to Streamlit!")
    st.subheader("Subheader: This is a subheader")
    st.text("This is a simple text display.")
    
    # Displaying markdown
    st.markdown("**Bold Text** and *Italic Text*")
    
    # Displaying code
    code = """
    def hello_world():
        print("Hello, World!")
    """
    st.code(code, language='python')
    
    # Displaying LaTeX
    st.latex(r"""
        E = mc^2
    """)