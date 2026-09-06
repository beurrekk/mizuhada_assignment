import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_gsheets import GSheetsConnection

# Set Streamlit wide mode
st.set_page_config(layout="wide")

st.title(":blue[MizuMi] TIKTOK PERFORMANCE")
st.text("by Suphannika")



allproduct_conn = st.connection("allproduct_gsheet", type=GSheetsConnection)
allproduct_df = allproduct_conn.read(ttl=21600)

affiliate_conn = st.connection("affiliate_gsheet", type=GSheetsConnection)
affiliate_df = affiliate_conn.read(ttl=21600)

mcn_conn = st.connection("mcn_gsheet", type=GSheetsConnection)
mcn_df = mcn_conn.read(ttl=21600)

kalodata_conn = st.connection("kalodata_gsheet", type=GSheetsConnection)
kalodata_df = kalodata_conn.read(ttl=21600)


st.write("All Product:", allproduct_df.shape)
st.write("Affiliate:", affiliate_df.shape)
st.write("MCN:", mcn_df.shape)
st.write("Kalodata:", kalodata_df.shape)
