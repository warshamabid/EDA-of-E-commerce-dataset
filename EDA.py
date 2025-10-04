# ecommerce_app.py
# Streamlit App: EDA for E-commerce Dataset

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io  # ✅ added for df.info() fix

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(page_title="E-commerce EDA Dashboard", layout="wide")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    # Replace with your actual dataset path if using locally
    df = pd.read_csv("ecommerce_dataset.csv")
    return df

df = load_data()

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("🛒 E-commerce Dashboard")
page = st.sidebar.radio(
    "Select Section",
    [
        "Dataset Overview",
        "Statistics",
        "Histograms & Boxplots",
        "Correlation Heatmap",
        "Category Analysis",
        "Region Analysis",
        "Payment Methods",
        "Advanced Visualizations"
    ]
)

# ------------------------------
# 1. Dataset Overview
# ------------------------------
if page == "Dataset Overview":
    st.title("📑 Dataset Overview")
    st.write("Preview of the dataset:")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

# ------------------------------
# 2. Statistics
# ------------------------------
elif page == "Statistics":
    st.title("📊 Descriptive Statistics")
    st.write(df.describe())

# ------------------------------
# 3. Histograms & Boxplots
# ------------------------------
elif page == "Histograms & Boxplots":
    st.title("📈 Histograms & Boxplots")

    numeric_cols = df.select_dtypes(include=np.number).columns
    selected_col = st.selectbox("Select numeric column:", numeric_cols)

    st.subheader(f"Histogram of {selected_col}")
    fig, ax = plt.subplots()
    sns.histplot(df[selected_col], kde=True, bins=20, ax=ax)
    st.pyplot(fig)

    st.subheader(f"Boxplot of {selected_col}")
    fig, ax = plt.subplots()
    sns.boxplot(x=df[selected_col], ax=ax)
    st.pyplot(fig)

# ------------------------------
# 4. Correlation Heatmap
# ------------------------------
elif page == "Correlation Heatmap":
    st.title("🔗 Correlation Heatmap")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ------------------------------
# 5. Category Analysis
# ------------------------------
elif page == "Category Analysis":
    st.title("📦 Category Analysis")

    st.subheader("Orders by Category")
    fig, ax = plt.subplots()
    sns.countplot(x="category", data=df, ax=ax, palette="Set2")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Revenue by Category")
    cat_revenue = df.groupby("category")["price"].sum().reset_index()
    fig = px.bar(cat_revenue, x="category", y="price", title="Revenue by Category", color="category")
    st.plotly_chart(fig)

# ------------------------------
# 6. Region Analysis
# ------------------------------
elif page == "Region Analysis":
    st.title("🌍 Region Analysis")

    st.subheader("Orders by Region")
    fig = px.histogram(df, x="region", title="Orders by Region", color="region")
    st.plotly_chart(fig)

# ------------------------------
# 7. Payment Methods
# ------------------------------
elif page == "Payment Methods":
    st.title("💳 Payment Method Insights")

    st.subheader("Payment Method Distribution")
    fig = px.pie(df, names="payment_method", title="Payment Method Share")
    st.plotly_chart(fig)

# ------------------------------
# 8. Advanced Visualizations
# ------------------------------
elif page == "Advanced Visualizations":
    st.title("⚡ Advanced Visualizations")

    st.subheader("Violin Plot: Price by Category")
    fig = px.violin(df, x="category", y="price", box=True, points="all", color="category")
    st.plotly_chart(fig)

    st.subheader("Revenue by Region (Interactive)")
    region_revenue = df.groupby("region")["price"].sum().reset_index()
    fig = px.bar(region_revenue, x="region", y="price", color="region", title="Revenue by Region")
    st.plotly_chart(fig)

# ------------------------------
# Footer
# ------------------------------
st.sidebar.markdown("---")
st.sidebar.info("Developed with ❤️ using Streamlit")
