import streamlit as st
import pandas as pd

# Import your utility functions
from utils.data_loader import load_data
from utils.validation import validate_order_totals, validate_channel_share
from utils.kpi_calculator import (
    calculate_dependency_index,
    calculate_diversification_score,
    calculate_channel_market_share
)

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="SkyCity Channel Intelligence",
    layout="wide",
    page_icon="📊"
)

st.title("📊 SkyCity Channel Intelligence Dashboard")

st.markdown("""
Multi-Channel Performance & Market Share Analytics Dashboard
Developed under Unified Mentor x SkyCity Auckland Collaboration
""")

# ==========================================================
# LOAD & PREP DATA
# ==========================================================
@st.cache_data
def load_and_prepare():
    df = load_data()

    # Data validation
    df = validate_order_totals(df)
    df = validate_channel_share(df)

    # KPI calculations
    df = calculate_dependency_index(df)
    df = calculate_diversification_score(df)

    return df

df = load_and_prepare()

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================
st.sidebar.header("🔍 Global Filters")

subregion_filter = st.sidebar.multiselect(
    "Subregion",
    options=sorted(df["Subregion"].dropna().unique()),
    default=sorted(df["Subregion"].dropna().unique())
)

cuisine_filter = st.sidebar.multiselect(
    "Cuisine Type",
    options=sorted(df["CuisineType"].dropna().unique()),
    default=sorted(df["CuisineType"].dropna().unique())
)

segment_filter = st.sidebar.multiselect(
    "Business Segment",
    options=sorted(df["Segment"].dropna().unique()),
    default=sorted(df["Segment"].dropna().unique())
)

# ==========================================================
# APPLY FILTERS
# ==========================================================
df_filtered = df[
    (df["Subregion"].isin(subregion_filter)) &
    (df["CuisineType"].isin(cuisine_filter)) &
    (df["Segment"].isin(segment_filter))
]

# Save to session state (FIXED)
st.session_state["filtered_data"] = df_filtered

# ==========================================================
# EXECUTIVE KPI SECTION
# ==========================================================
st.subheader("📊 Executive Summary KPIs")

total_orders = df_filtered["MonthlyOrders"].sum()
# total_restaurants = df_filtered["RestaurantsID"].nunique()
avg_aov = df_filtered["AOV"].mean()

shares = calculate_channel_market_share(df_filtered)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", f"{total_orders:,}")
# col2.metric("RestaurantsID", total_restaurants)
col3.metric("Avg AOV", f"${avg_aov:.2f}")
col4.metric("Dependency Index", f"{df_filtered['AggregatorDependence'].mean():.2f}")

st.divider()

# ==========================================================
# CHANNEL SHARE KPI
# ==========================================================
st.subheader("📊 Channel Share Distribution")

col1, col2, col3, col4 = st.columns(4)

col1.metric("In-Store Share", f"{shares['InStore']:.2%}")
col2.metric("Uber Eats Share", f"{shares['UberEats']:.2%}")
col3.metric("DoorDash Share", f"{shares['DoorDash']:.2%}")
col4.metric("Self Delivery Share", f"{shares['SelfDelivery']:.2%}")

# ==========================================================
# VISUALIZATION SECTION
# ==========================================================
st.subheader("📈 Channel Orders Breakdown")

channel_data = pd.DataFrame({
    "Channel": ["InStore", "UberEats", "DoorDash", "SelfDelivery"],
    "Orders": [
        df_filtered["InStoreOrders"].sum(),
        df_filtered["UberEatsOrders"].sum(),
        df_filtered["DoorDashOrders"].sum(),
        df_filtered["SelfDeliveryOrders"].sum()
    ]
})

st.bar_chart(channel_data.set_index("Channel"))

# ==========================================================
# DEPENDENCY & DIVERSIFICATION
# ==========================================================
st.subheader("📉 Dependency & Diversification Insights")

col1, col2 = st.columns(2)

col1.metric(
    "Avg Aggregator Dependency",
    f"{df_filtered['AggregatorDependence'].mean():.2f}"
)

col2.metric(
    "Avg Diversification Score",
    f"{df_filtered['DiversificationScore'].mean():.2f}"
)

# ==========================================================
# DATA TABLE VIEW
# ==========================================================
st.subheader("📋 Filtered Dataset Preview")

st.dataframe(df_filtered.head(50), use_container_width=True)

# ==========================================================
# FOOTER
# ==========================================================
st.divider()
st.info("Use sidebar filters to explore different segments and regions.")
