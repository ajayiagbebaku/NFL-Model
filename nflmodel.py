import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 10 Projections: Updated 11/11/2021.")
st.text("Lines Vegas Lines updated Sunday morning")
st.text("Spread Win/Loss: (4-9).308")
st.text("Over/Under Win Loss: (6-7).462")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)