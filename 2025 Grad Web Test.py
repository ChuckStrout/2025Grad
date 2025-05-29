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
#st.write(dfg)

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
    st.header("Starting in the PAC ")
    
    sectg=selected_row["SECTION"]
    st.text(f"Sit in the {sectg} Section")
    rowg=selected_row["PROW"]
    st.text(f"Sit in Row: {rowg}")
    snumg=selected_row["PSEAT NUMBER"]
    st.text(f"Sit in Seat Number: {snumg}" )

if venue =="On Turf" and event == "Graduation":
    selected_row = dfg[dfg["Full Name"] == selected_name].iloc[0]
    st.header("On The Turf")
    side=selected_row["SIDE"]
    st.text(f"You will be On the Side: {side}")
    rowg=selected_row["ROW"]
    st.text(f"You will Sit in the Row: {rowg}" )
    sng=selected_row["SEAT NUMBER"]
    st.text(f"Sit in Seat Number: {sng}")


#Lane	Number	Turn	Section	Row	Seat

# Class Day
if venue == "In Field House" and event == "Class Day":
    selected_row = dfc[dfc["Full Name"] == selected_name].iloc[0]
    st.header("For Class Day, Starting in the Field House ")
    lane=selected_row["Lane"]
    st.text(f"You will be in the {lane}")
    numb=selected_row["Number"]
    st.text(f"You will be number {numb} in that row")
    st.title(f"{lane}         -       {numb}")

    
if venue =="In the Auditorium" and event == "Class Day":
    selected_row = dfc[dfc["Full Name"] == selected_name].iloc[0]
    st.header("In the Auditorium")
    
    turn=selected_row["Turn"]
    sect=selected_row["Section"]
    row=selected_row["Row"]
    st.subheader("To Sit in Your Seat:")
    st.text(f"{turn} and enter the Row {row} of the {sect} Section")

    sn=selected_row["Seat"]
    st.text(f"Sit in Seat Number: {sn}")

st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text("v0529259:27")
