# ecommerce_dashboard.py
# Streamlit App: Full E-Commerce EDA Dashboard (All-in-One Page)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import io

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(page_title="E-commerce EDA Dashboard", layout="wide")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_dataset.csv")
    return df

df = load_data()

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("🛍️ E-commerce Dashboard")
st.sidebar.markdown("Analyze your sales, categories, and customers in one place.")
st.sidebar.markdown("---")
st.sidebar.info("Developed with ❤️ using Streamlit & Plotly")

# ------------------------------
# Title
# ------------------------------
st.title("📊 E-Commerce Exploratory Data Analysis Dashboard")
st.markdown("### Interactive Insights of Sales, Categories, Regions, and Payment Trends")

# ------------------------------
# Dataset Overview
# ------------------------------
st.header("📑 Dataset Overview")
st.dataframe(df.head(), use_container_width=True)

buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

# ------------------------------
# Missing Values
# ------------------------------
st.header("🚨 Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]
fig_missing = px.bar(
    missing, 
    x="Column", 
    y="Missing Values", 
    title="Missing Values per Column",
    color="Missing Values", 
    color_continuous_scale="Reds"
)
st.plotly_chart(fig_missing, use_container_width=True)

# ------------------------------
# Descriptive Statistics
# ------------------------------
st.header("📈 Descriptive Statistics")
st.dataframe(df.describe().T, use_container_width=True)

# ------------------------------
# Correlation Heatmap
# ------------------------------
st.header("🔗 Correlation Analysis")
corr = df.corr(numeric_only=True)
fig_corr = px.imshow(
    corr, 
    text_auto=True, 
    color_continuous_scale="Viridis",
    title="Correlation Heatmap"
)
st.plotly_chart(fig_corr, use_container_width=True)

# ------------------------------
# Category Analysis
# ------------------------------
st.header("📦 Category Analysis")

# Orders by Category
category_counts = df["category"].value_counts().reset_index()
category_counts.columns = ["Category", "Orders"]
fig_cat_orders = px.bar(
    category_counts, 
    x="Category", 
    y="Orders",
    color="Category",
    title="Orders by Category",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
st.plotly_chart(fig_cat_orders, use_container_width=True)

# Revenue by Category
cat_revenue = df.groupby("category")["price"].sum().reset_index()
fig_cat_revenue = px.bar(
    cat_revenue, 
    x="category", 
    y="price", 
    color="category", 
    title="Revenue by Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_cat_revenue, use_container_width=True)

# ------------------------------
# Region Analysis
# ------------------------------
st.header("🌍 Regional Analysis")

region_orders = df["region"].value_counts().reset_index()
region_orders.columns = ["Region", "Orders"]
fig_region_orders = px.bar(
    region_orders, 
    x="Region", 
    y="Orders", 
    color="Region", 
    title="Orders by Region",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
st.plotly_chart(fig_region_orders, use_container_width=True)

region_revenue = df.groupby("region")["price"].sum().reset_index()
fig_region_revenue = px.choropleth(
    region_revenue, 
    locations="region", 
    locationmode="country names", 
    color="price", 
    title="Revenue Distribution by Region",
    color_continuous_scale="Blues"
)
st.plotly_chart(fig_region_revenue, use_container_width=True)

# ------------------------------
# Payment Method Insights
# ------------------------------
st.header("💳 Payment Method Insights")

fig_payment = px.pie(
    df, 
    names="payment_method", 
    title="Payment Method Distribution", 
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_payment, use_container_width=True)

# ------------------------------
# Advanced Visualizations
# ------------------------------
st.header("⚡ Advanced Visualizations")

fig_violin = px.violin(
    df, 
    x="category", 
    y="price", 
    box=True, 
    points="all", 
    color="category",
    title="Price Distribution by Category",
    color_discrete_sequence=px.colors.qualitative.Bold
)
st.plotly_chart(fig_violin, use_container_width=True)

# Revenue by Region (Interactive)
region_revenue = df.groupby("region")["price"].sum().reset_index()
fig_bar = px.bar(
    region_revenue, 
    x="region", 
    y="price", 
    color="region", 
    title="Total Revenue by Region",
    color_discrete_sequence=px.colors.qualitative.Dark2
)
st.plotly_chart(fig_bar, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("### 💡 *Dashboard built for interactive EDA of E-commerce data.*")
