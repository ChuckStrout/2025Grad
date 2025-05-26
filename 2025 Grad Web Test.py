import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("2025SMEUD.xlsx")

# Display the DataFrame in Streamlit
st.title("2025SMEUD.xlsx Viewer")
st.dataframe(df)