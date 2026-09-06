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




    
df = allproduct_df.copy()

# Clean datetime
df["Created Time"] = pd.to_datetime(
    df["Created Time"],
    errors="coerce"
)

# Clean revenue
df["SKU Subtotal After Discount"] = pd.to_numeric(
    df["SKU Subtotal After Discount"],
    errors="coerce"
).fillna(0)

# Create month
df["Month"] = df["Created Time"].dt.to_period("M")


# =========================
# Get number of days
# from ALL orders
# =========================

month_days = (
    df.dropna(subset=["Created Time"])
    .groupby("Month")
    .agg(
        Start_Date=("Created Time", "min"),
        End_Date=("Created Time", "max")
    )
    .reset_index()
)

month_days["Days"] = (
    month_days["End_Date"].dt.normalize()
    - month_days["Start_Date"].dt.normalize()
).dt.days + 1


# =========================
# Filter Completed only
# =========================

completed_df = df[
    df["Order Status"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["completed", "complete"])
].copy()


# =========================
# Monthly summary
# =========================

monthly_summary = (
    completed_df
    .groupby("Month")
    .agg(
        Completed_Orders=("Order ID", "nunique"),
        Revenue=("SKU Subtotal After Discount", "sum")
    )
    .reset_index()
)

# Merge days
monthly_summary = monthly_summary.merge(
    month_days[["Month", "Days"]],
    on="Month",
    how="left"
)

# Avg Daily Revenue
monthly_summary["Avg Daily Revenue"] = (
    monthly_summary["Revenue"]
    / monthly_summary["Days"]
)

# Growth vs previous month
monthly_summary["Growth"] = (
    monthly_summary["Avg Daily Revenue"]
    .pct_change()
    * 100
)

# Month display
monthly_summary["Month"] = (
    monthly_summary["Month"]
    .dt.strftime("%b %Y")
)


# =========================
# Rename for display
# =========================

display_df = monthly_summary.rename(
    columns={
        "Completed_Orders": "Completed Orders"
    }
)


# =========================
# Streamlit table
# =========================

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
            format="฿%.0f"
        ),

        "Days": st.column_config.NumberColumn(
            "Days",
            format="%d"
        ),

        "Avg Daily Revenue": st.column_config.NumberColumn(
            "Avg Daily Revenue",
            format="฿%.0f"
        ),

        "Growth": st.column_config.NumberColumn(
            "Growth",
            format="%.2f%%"
        ),
    }
)
