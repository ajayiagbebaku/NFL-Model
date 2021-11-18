import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 11 Projections: Updated 11/17/2021.")
st.text("Vegas lines updated Sunday morning")
st.text("Spread Win/Loss: (10-17).37")
st.text("Over/Under Win Loss: (13-14).481")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)