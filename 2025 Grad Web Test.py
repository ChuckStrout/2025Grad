import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Load the Excel file
DATA_FILENAME = Path(__file__).parent/'data/2025GRD.csv'
df = pd.read_csv(DATA_FILENAME)


# Display the DataFrame in Streamlit
st.title("2025 RGD Viewer")
st.dataframe(df)