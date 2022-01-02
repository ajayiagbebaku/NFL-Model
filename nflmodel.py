import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 17 Projections: Updated 1/2/2022.")
st.text("Final Projections are on Sunday morning")
st.text("Spread Win/Loss: (58-50).537")
st.text("Over/Under Win Loss: (49-64).434")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)