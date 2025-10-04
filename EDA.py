# ecommerce_eda_dashboard.py
# Streamlit EDA Dashboard (All in One Page | Plotly Only | Professional Layout)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import io

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="E-commerce EDA Dashboard",
    layout="wide",
    page_icon="🛒",
)

st.title("🛒 E-commerce Data Analysis Dashboard")
st.markdown(
    """
    This interactive dashboard provides a complete Exploratory Data Analysis (EDA) 
    of your **E-commerce dataset** using interactive and visually rich **Plotly** charts.  
    ---
    """
)

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_dataset.csv")
    return df

df = load_data()

# ------------------------------
# Dataset Overview
# ------------------------------
st.header("📋 Dataset Overview")

st.write("Preview of your dataset:")
st.dataframe(df.head())

# Dataset Info
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()

with st.expander("View Dataset Information"):
    st.text(info_str)

# Missing Values
st.subheader("🧩 Missing Values")
missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Column", "Missing Values"]
fig_missing = px.bar(
    missing_df,
    x="Column",
    y="Missing Values",
    color="Missing Values",
    color_continuous_scale="RdYlBu",
    title="Missing Values per Column",
)
st.plotly_chart(fig_missing, use_container_width=True)

# ------------------------------
# Summary Statistics
# ------------------------------
st.header("📊 Descriptive Statistics")

st.write(df.describe())

# ------------------------------
# Visual Explorations
# ------------------------------
st.header("📈 Key Visual Insights")

# 1. Revenue by Category
st.subheader("💰 Revenue by Category")
cat_revenue = df.groupby("category")["price"].sum().reset_index()
fig_cat = px.bar(
    cat_revenue,
    x="category",
    y="price",
    color="category",
    title="Total Revenue by Product Category",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig_cat.update_layout(xaxis_title="Category", yaxis_title="Total Revenue")
st.plotly_chart(fig_cat, use_container_width=True)

# 2. Revenue by Region
st.subheader("🌍 Revenue by Region")
region_revenue = df.groupby("region")["price"].sum().reset_index()
fig_region = px.bar(
    region_revenue,
    x="region",
    y="price",
    color="region",
    title="Revenue Distribution Across Regions",
    color_discrete_sequence=px.colors.sequential.Aggrnyl
)
st.plotly_chart(fig_region, use_container_width=True)

# 3. Payment Method Distribution
st.subheader("💳 Payment Method Distribution")
fig_payment = px.pie(
    df,
    names="payment_method",
    title="Share of Payment Methods Used",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_payment, use_container_width=True)

# 4. Price Distribution
st.subheader("📦 Price Distribution")
fig_price = px.histogram(
    df,
    x="price",
    nbins=30,
    title="Distribution of Product Prices",
    color_discrete_sequence=["#2E91E5"]
)
st.plotly_chart(fig_price, use_container_width=True)

# 5. Violin Plot: Price by Category
st.subheader("🎻 Price Distribution by Category (Violin Plot)")
fig_violin = px.violin(
    df,
    x="category",
    y="price",
    box=True,
    points="all",
    color="category",
    color_discrete_sequence=px.colors.qualitative.Safe,
    title="Price Variability within Each Category"
)
st.plotly_chart(fig_violin, use_container_width=True)

# 6. Correlation Heatmap
st.subheader("🔗 Correlation Heatmap")
corr = df.corr(numeric_only=True)
fig_corr = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Between Numerical Features"
)
st.plotly_chart(fig_corr, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown(
    """
    ✅ **Dashboard Summary:**  
    - Provides dataset overview, missing value report, and descriptive stats  
    - Visualizes key patterns in revenue, region, category, and price  
    - All visuals are **interactive** and color-enhanced for clarity  
    ---
    **Developed with ❤️ using Streamlit & Plotly**
    """
)
