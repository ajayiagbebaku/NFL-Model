import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 12 Projections: Updated 11/25/2021.")
st.text("Vegas lines updated Sunday morning")
st.text("Spread Win/Loss: (19-23).452")
st.text("Over/Under Win Loss: (18-24).429")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)