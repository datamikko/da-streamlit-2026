import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    return pd.read_csv("https://pxdata.stat.fi/PxWeb/sq/7ed4e369-dfce-4881-b508-3661eb487d4d", encoding="latin-1")


df = load_data()

st.markdown(
'''# Flights to Lapland

Arrivals from international airports to Lapland airports
''')

st.dataframe(df)

st.divider()

st.markdown(
'''## Line chart of selected airport
''')

option = st.selectbox(
    "Select airport",
    ("Total Rovaniemi", "Total Kittilä"),
)
# st.write(option)

st.line_chart(df, x="Year", y=option)