import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")

st.title(":blue[MizuMi] TIKTOK PERFORMANCE")
st.text("by Suphannika")


########################################################################
########################## Load data ###################################
########################################################################


@st.cache_data(ttl="6h")
def load_data():

    allproduct_conn = st.connection("allproduct_gsheet",type=GSheetsConnection)
    allproduct_df = allproduct_conn.read()

    affiliate_conn = st.connection("affiliate_gsheet",type=GSheetsConnection)
    affiliate_df = affiliate_conn.read()

    mcn_conn = st.connection("mcn_gsheet",type=GSheetsConnection)
    mcn_df = mcn_conn.read()

    kalodata_conn = st.connection("kalodata_gsheet",type=GSheetsConnection)
    kalodata_df = kalodata_conn.read()

    return allproduct_df, affiliate_df, mcn_df, kalodata_df

allproduct_df, affiliate_df, mcn_df, kalodata_df = load_data()





########################################################################
########################## Overall ####################################
########################################################################




    
display_df = monthly_summary.rename(
    columns={
        "Completed_Orders": "Completed Orders",
        "Revenue": "Revenue",
        "Active_Days": "Days",
        "Avg Daily Revenue": "Avg Daily Revenue",
        "Growth": "Growth"
    }
)

st.subheader("Monthly Revenue Performance — Completed Orders")

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Month": st.column_config.TextColumn(
            "Month"
        ),

        "Completed Orders": st.column_config.NumberColumn(
            "Completed Orders",
            format="%d"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="฿%,.0f"
        ),

        "Days": st.column_config.NumberColumn(
            "Days",
            format="%d"
        ),

        "Avg Daily Revenue": st.column_config.NumberColumn(
            "Avg Daily Revenue",
            format="฿%,.0f"
        ),

        "Growth": st.column_config.NumberColumn(
            "Growth",
            format="%.2f%%"
        ),
    }
)








