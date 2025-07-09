import streamlit as st

def layout_design():
    st.title("Layout Design Example")
    
    # Sidebar
    st.sidebar.header("Sidebar")
    st.sidebar.write("This is the sidebar content.")
    
    # Main content
    st.header("Main Content")
    st.write("This is the main content area.")
    
    # Columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Column 1")
        st.write("Content for column 1.")
    
    with col2:
        st.subheader("Column 2")
        st.write("Content for column 2.")
    
    # Expander
    with st.expander("More Information"):
        st.write("This is additional information inside an expander.")