import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Load the Excel file
DATA_FILENAME = Path(__file__).parent/'data/2025 GSMUD.xlsx'
dfboth = pd.read_excel(DATA_FILENAME)
dfg = pd.read_excel(DATA_FILENAME, sheet_name="Grad Raw Data")
dfg.columns.values[1] = "PROW"
dfg.columns.values[2] = "PSEAT NUMBER"
dfg.columns.values[4] = "ROW"
dfg.columns.values[5] = "SEAT NUMBER"
dfc = pd.read_excel(DATA_FILENAME, sheet_name= "CD Data")
# Display the DataFrame in Streamlit
st.title("2025 RMHS Seating System")
st.write(dfg)

event = st.radio("Select Event",("Graduation", "Class Day"))
if event == "Graduation":
    venue_options = ("In PAC", "On Turf")
else:
    venue_options = ("In Field House", "In the Auditorium")
venue = st.radio("Select Venue", venue_options)

dfg["Full Name"] = dfg["Last Name"].astype(str) + ", " + dfg["First Name"].astype(str)
dfc["Full Name"] = dfc["Last Name"].astype(str) + ", " + dfc["First Name"].astype(str)
if event == "Graduation":
    selected_name = st.selectbox(
        "Select Your Name",
        options=sorted(dfg["Full Name"].unique()),
        key="full_name_select"
    )
else:
        selected_name = st.selectbox(
        "Select Your Name",
        options=sorted(dfc["Full Name"].unique()),
        key="full_name_select"
        )

# Graduation
if venue == "In PAC" and event == "Graduation":
    selected_row = dfg[dfg["Full Name"] == selected_name].iloc[0]
    st.subheader("Starting in the PAC ")
    st.text_input("Sit in the Section:", value=selected_row["SECTION"], disabled=True)
    st.text_input("Sit in Row:", value=selected_row["PROW"], disabled=True)
    st.text_input("Sit in Seat Number:", value=selected_row["PSEAT NUMBER"], disabled=True)
if venue =="On Turf" and event == "Graduation":
    selected_row = dfg[dfg["Full Name"] == selected_name].iloc[0]
    st.subheader("On The Turf")
    st.text_input("You will be On the Side:", value=selected_row["SIDE"], disabled=True)
    st.text_input("You will Sit in the Row:", value=selected_row["ROW"], disabled=True)
    st.text_input("Sit in Seat Number:", value=selected_row["SEAT NUMBER"], disabled=True)


#Lane	Number	Turn	Section	Row	Seat

# Class Day
if venue == "In Field House" and event == "Class Day":
    selected_row = dfc[dfc["Full Name"] == selected_name].iloc[0]
    st.subheader("Starting in the Field House ")
    st.text_input("Start in the Lane", value=selected_row["Lane"], disabled=True)
    st.text_input("You are number:", value=selected_row["Number"], disabled=True)
    
if venue =="In the Auditorium" and event == "Class Day":
    selected_row = dfc[dfc["Full Name"] == selected_name].iloc[0]
    st.subheader("In the Auditorium")
    st.text_input("You will be in the Lane:", value=selected_row["Lane"], disabled=True)
    st.text_input("To Sit in Your Seat TURN:", value=selected_row["Turn"], disabled=True)
    st.text_input("You will Sit in the Section:", value=selected_row["Section"], disabled=True)
    st.text_input("Sit in Seat Number:", value=selected_row["Seat"], disabled=True)