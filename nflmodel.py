import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 15 Projections: Updated 12/16/2021.")
st.text("Final Projections are on Sunday morning")
st.text("Spread Win/Loss: (44-40).524")
st.text("Over/Under Win Loss: (41-44).482")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)