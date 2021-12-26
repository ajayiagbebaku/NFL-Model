import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 16 Projections: Updated 12/26/2021.")
st.text("Final Projections are on Sunday morning")
st.text("Spread Win/Loss: (54-46).540")
st.text("Over/Under Win Loss: (45-56).482")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)