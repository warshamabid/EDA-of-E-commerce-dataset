# ecommerce_app.py
# Streamlit App: Professional & Colorful Single-Page E-commerce EDA Dashboard

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
    page_icon="🛍️",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2331/2331970.png", width=100)
st.sidebar.title("📊 E-commerce Dashboard")
st.sidebar.markdown("Explore interactive visualizations below 👇")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_dataset.csv")
    return df

df = load_data()

# ------------------------------
# Dashboard Title
# ------------------------------
st.markdown(
    "<h1 style='text-align:center; color:#FF6B35;'>🛒 E-commerce Data Analysis Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr style='border:2px solid #FF6B35;'>", unsafe_allow_html=True)

# ------------------------------
# KPIs Section
# ------------------------------
st.subheader("📌 Key Performance Indicators")

total_revenue = df["price"].sum()
total_orders = len(df)
avg_price = df["price"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("📦 Total Orders", f"{total_orders:,}")
col3.metric("🏷️ Average Price", f"${avg_price:,.2f}")

# ------------------------------
# Dataset Overview
# ------------------------------
st.header("📑 Dataset Overview")
st.dataframe(df.head())

buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

st.subheader("❌ Missing Values")
st.write(df.isnull().sum())

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
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig_cat.update_layout(plot_bgcolor="#FFF", paper_bgcolor="#FFF", title_font_color="#FF6B35")
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
    color_discrete_sequence=px.colors.qualitative.Pastel2
)
fig_orders.update_layout(plot_bgcolor="#FFF", paper_bgcolor="#FFF", title_font_color="#FF6B35")
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
    color_continuous_scale="Turbo",  # 🔥 More vibrant scale
    title="Global Revenue Distribution by Region"
)
fig_map.update_layout(
    geo_bgcolor="#EAF6FF",
    paper_bgcolor="#FFF",
    title_font_color="#FF6B35"
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
    hole=0.35,
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_pay.update_layout(paper_bgcolor="#FFF", title_font_color="#FF6B35")
st.plotly_chart(fig_pay, use_container_width=True)

# ------------------------------
# Price Distribution by Category
# ------------------------------
st.header("💰 Price Distribution by Category")
fig_price = px.violin(
    df,
    x="category",
    y="price",
    box=True,
    points="all",
    color="category",
    title="Price Distribution by Category",
    color_discrete_sequence=px.colors.qualitative.Dark24
)
fig_price.update_layout(paper_bgcolor="#FFF", plot_bgcolor="#FFF", title_font_color="#FF6B35")
st.plotly_chart(fig_price, use_container_width=True)

# ------------------------------
# Correlation Heatmap
# ------------------------------
st.header("📊 Correlation Heatmap")
corr = df.corr(numeric_only=True)
fig_heat = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Plasma",  # bright gradient
    title="Correlation Matrix of Numeric Variables"
)
fig_heat.update_layout(paper_bgcolor="#FFF", plot_bgcolor="#FFF", title_font_color="#FF6B35")
st.plotly_chart(fig_heat, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("<hr style='border:2px solid #FF6B35;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Developed with ❤️ by <b>WARSHAM ABID</b> | Powered by Streamlit + Plotly</p>", unsafe_allow_html=True)
