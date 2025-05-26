import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_csv("2025RGD.csv")

# Display the DataFrame in Streamlit
st.title("2025 RGD Viewer")
st.dataframe(df)