import streamlit as st

def display_data():
    st.title("Displaying Data Example")
    
    # Sample data
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    
    # Display data as a table
    st.subheader("Data Table")
    st.table(data)
    
    # Display data as a dataframe
    st.subheader("DataFrame")
    df = st.dataframe(data)
    
    # Display data as a JSON object
    st.subheader("JSON Data")
    st.json(data)