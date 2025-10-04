# ecommerce_app.py
# Streamlit App: Professional Single-Page E-commerce EDA Dashboard

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
    page_icon="🛍️"
)

st.title("🛍️ E-commerce Data Analysis Dashboard")
st.markdown("### Explore sales, revenue, and customer trends interactively with Plotly visualizations.")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2331/2331970.png", width=100)
st.sidebar.title("📊 Dashboard Controls")

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
st.header("📑 Dataset Overview")
st.dataframe(df.head())

# Dataset Info
st.subheader("ℹ️ Dataset Information")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

# Missing Values
st.subheader("❌ Missing Values")
st.write(df.isnull().sum())

# ------------------------------
# Key Statistics
# ------------------------------
st.header("📈 Key Statistics")
st.dataframe(df.describe())

# ------------------------------
# Revenue by Category
# ------------------------------
st.header("💸 Revenue by Category")

cat_revenue = df.groupby("category")["price"].sum().reset_index().sort_values("price", ascending=False)

fig_cat = px.bar(
    cat_revenue,
    x="category",
    y="price",
    color="category",
    text_auto=".2s",
    title="Total Revenue by Product Category",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_cat.update_traces(textfont_size=12)
st.plotly_chart(fig_cat, use_container_width=True)

# ------------------------------
# Orders by Category
# ------------------------------
st.header("📦 Orders by Category")
fig_orders = px.histogram(
    df,
    x="category",
    color="category",
    title="Number of Orders by Category",
    color_discrete_sequence=px.colors.qualitative.Safe
)
st.plotly_chart(fig_orders, use_container_width=True)

# ------------------------------
# Revenue by Region (Map)
# ------------------------------
st.header("🌍 Revenue by Region (Interactive Map)")
region_revenue = df.groupby("region")["price"].sum().reset_index()

fig_map = px.choropleth(
    region_revenue,
    locations="region",
    locationmode="country names",
    color="price",
    hover_name="region",
    color_continuous_scale="Rainbow",
    title="Global Revenue Distribution by Region"
)
st.plotly_chart(fig_map, use_container_width=True)

# ------------------------------
# Payment Method Insights
# ------------------------------
st.header("💳 Payment Method Insights")
payment_data = df["payment_method"].value_counts().reset_index()
payment_data.columns = ["Payment Method", "Count"]

fig_pay = px.pie(
    payment_data,
    names="Payment Method",
    values="Count",
    title="Payment Method Distribution",
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_pay, use_container_width=True)

# ------------------------------
# Price Distribution
# ------------------------------
st.header("💰 Price Distribution")
fig_price = px.violin(
    df,
    x="category",
    y="price",
    box=True,
    points="all",
    color="category",
    title="Price Distribution by Category",
    color_discrete_sequence=px.colors.qualitative.Prism
)
st.plotly_chart(fig_price, use_container_width=True)

# ------------------------------
# Correlation Heatmap
# ------------------------------
st.header("📊 Correlation Heatmap")
corr = df.corr(numeric_only=True)
fig_heat = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Tealrose",
    title="Correlation Matrix of Numeric Variables"
)
st.plotly_chart(fig_heat, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("✅ **Developed with ❤️ by WARSHAM** | Interactive E-commerce Insights Dashboard using Streamlit + Plotly")
