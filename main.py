import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_gsheets import GSheetsConnection

# Set Streamlit wide mode
st.set_page_config(layout="wide")

st.title(":blue[MizuMi] TIKTOK PERFORMANCE")
st.text("by Suphannika")

allproduct_conn = st.connection("allproduct_gsheet", type=GSheetsConnection)
df = allproduct_conn.read()

st.dataframe(df)
