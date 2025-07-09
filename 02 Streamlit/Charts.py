import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def charts_example():
    df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
    st.dataframe(df)

    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)

    
    fig, ax = plt.subplots()
    ax.plot(df["A"])
    st.pyplot(fig)


