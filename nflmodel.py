import pandas as pd
import streamlit as st
import numpy
st.set_page_config(page_title="NFL Projections 2021",layout="wide")
st.header("Week 13 Projections: Updated 12/9/2021.")
st.text("Final Projections are on Sunday morning")
st.text("Spread Win/Loss: (35-36).493")
st.text("Over/Under Win Loss: (33-38).465")
df = pd.read_excel("UpdatedResultsNFL.xlsx")
st.dataframe(df)