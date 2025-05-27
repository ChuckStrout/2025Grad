import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Load the Excel file
DATA_FILENAME = Path(__file__).parent/'data/2025GRD.csv'
df = pd.read_csv(DATA_FILENAME)


# Display the DataFrame in Streamlit
st.title("2025 RMHS")
st.title("Graduation Seating System")
venue = st.radio("Select Venue", ("In PAC", "On Turf"))
df["Full Name"] = df["Last Name"].astype(str) + ", " + df["First Name"].astype(str)
selected_name = st.selectbox(
    "Select Your Name",
    options=sorted(df["Full Name"].unique()),
    key="full_name_select"
)

if venue == "In PAC":
    selected_row = df[df["Full Name"] == selected_name].iloc[0]
    st.subheader("Starting in the PAC ")
    st.text_input("Sit in the Section:", value=selected_row["SECTION"], disabled=True)
    st.text_input("Sit in Row:", value=selected_row["PROW"], disabled=True)
    st.text_input("Sit in Seat Number:", value=selected_row["PSEAT NUMBER"], disabled=True)
if venue =="On Turf":
    selected_row = df[df["Full Name"] == selected_name].iloc[0]
    st.subheader("On The Turf")
    st.text_input("You will be On the Side:", value=selected_row["SIDE"], disabled=True)
    st.text_input("Sit in Row:", value=selected_row["ROW"], disabled=True)
    st.text_input("Sit in Seat Number:", value=selected_row["SEAT NUMBER"], disabled=True)