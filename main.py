import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")

st.title(":blue[MizuMi] TIKTOK PERFORMANCE")
st.text("by Suphannika")

allproduct_conn = st.connection(
    "allproduct_gsheet",
    type=GSheetsConnection
)
allproduct_df = allproduct_conn.read()

affiliate_conn = st.connection(
    "affiliate_gsheet",
    type=GSheetsConnection
)
affiliate_df = affiliate_conn.read()

mcn_conn = st.connection(
    "mcn_gsheet",
    type=GSheetsConnection
)
mcn_df = mcn_conn.read()

kalodata_conn = st.connection(
    "kalodata_gsheet",
    type=GSheetsConnection
)
kalodata_df = kalodata_conn.read()

st.write(allproduct_df)
st.write(affiliate_df)
st.write(mcn_df)
st.write(kalodata_df)
