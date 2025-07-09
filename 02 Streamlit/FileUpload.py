import streamlit as st

def file_upload():
    st.title("File Upload Example")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "pdf"])
    
    if uploaded_file is not None:
        # Display the file name
        st.write(f"File name: {uploaded_file.name}")
        
        # Read and display the content of the file
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File Content", content, height=300)
        else:
            st.write("File type not supported for display.")