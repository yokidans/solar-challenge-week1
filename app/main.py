import streamlit as st
import plotly.express as px
from utils import load_data, filter_regions

# --- Configuration ---
st.set_page_config(layout="wide")
COUNTRIES = ["benin", "togo", "ghana"]  # Add your countries

# --- Sidebar Widgets ---
selected_country = st.sidebar.selectbox("Select Country", COUNTRIES)
metric = st.sidebar.radio("Performance Metric", ["GHI", "DNI", "DHI"])
top_n = st.sidebar.slider("Top Regions", 3, 10, 5)

# --- Load Data ---
df = load_data(selected_country)
regions_df = filter_regions(df, metric, top_n)

# --- Dashboard Layout ---
col1, col2 = st.columns([3, 2])

with col1:
    st.header(f"{metric} Distribution")
    fig = px.box(df, y=metric, points="all")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.header(f"Top {top_n} Regions")
    st.dataframe(regions_df.style.highlight_max(axis=0))

    st.download_button(
        "Download Top Regions",
        data=regions_df.to_csv(index=False),
        file_name=f"top_regions_{selected_country}.csv"
    )
