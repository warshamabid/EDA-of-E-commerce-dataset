# ecommerce_app.py
# Streamlit App: EDA for E-commerce Dataset

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-commerce EDA", layout="wide")

st.title("🛒 E-commerce Data Analysis Dashboard")

# ------------------------------
# Upload or Load Demo Data
# ------------------------------
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ File uploaded successfully!")
else:
    st.sidebar.warning("⚠️ No file uploaded. Using demo dataset instead.")
    demo_data = {
        "OrderID": [1, 2, 3, 4, 5, 6],
        "Product": ["Shoes", "Shirt", "Laptop", "Phone", "Watch", "Shoes"],
        "Category": ["Fashion", "Fashion", "Electronics", "Electronics", "Accessories", "Fashion"],
        "Price": [50, 30, 1200, 800, 200, 55],
        "Quantity": [1, 2, 1, 1, 3, 1],
        "Revenue": [50, 60, 1200, 800, 600, 55]
    }
    df = pd.DataFrame(demo_data)

# ------------------------------
# Show Dataset
# ------------------------------
st.subheader("📑 Dataset Preview")
st.dataframe(df.head())

st.subheader("📊 Dataset Info")
st.write(df.describe())

# Missing Values
st.subheader("❌ Missing Values")
st.write(df.isnull().sum())

# ------------------------------
# Visualizations
# ------------------------------
st.subheader("📈 Visualizations")

# Price Distribution
st.write("### Distribution of Prices")
fig, ax = plt.subplots()
sns.histplot(df["Price"], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Category Count
st.write("### Category Count")
fig, ax = plt.subplots()
sns.countplot(x="Category", data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Revenue by Category
st.write("### Revenue by Category")
fig, ax = plt.subplots()
sns.barplot(x="Category", y="Revenue", data=df, estimator=sum, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ------------------------------
# Footer
# ------------------------------
st.sidebar.markdown("---")
st.sidebar.info("Developed with ❤️ using Streamlit")
