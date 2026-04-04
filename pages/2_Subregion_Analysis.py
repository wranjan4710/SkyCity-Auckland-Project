import streamlit as st
import pandas as pd
import plotly.express as px
# from utils.data_loader import load_data
# from components.sidebar import sidebar_filters

st.title("🌍🌍 Subregion Analysis")

df = st.session_state.get("filtered_data")

if df is None:
    st.warning("Please run the main dashboard first.")
    st.stop()

subregion_channel = df.groupby("Subregion")[[
    "InStoreOrders",
    "UberEatsOrders",
    "DoorDashOrders",
    "SelfDeliveryOrders"
]].sum().reset_index()

melted = subregion_channel.melt(
    id_vars="Subregion",
    var_name="Channel",
    value_name="Orders"
)

fig = px.density_heatmap(
    melted,
    x="Channel",
    y="Subregion",
    z="Orders",
    color_continuous_scale="Blues",
    title="Channel Dominance Across Subregion"
)

st.plotly_chart(fig, use_container_width=True)
