# ecommerce_app.py
# Streamlit App: EDA for E-commerce Dataset

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/ecommerce.csv")  # place your dataset in /data folder
    return df

df = load_data()

st.title("🛒 E-commerce Data Analysis Dashboard")

st.write("## Dataset Preview")
st.dataframe(df.head())

# ------------------------------
# Basic EDA
# ------------------------------
st.write("### Dataset Info")
st.write(df.describe())

# Missing values
st.write("### Missing Values")
st.write(df.isnull().sum())

# ------------------------------
# Visualization
# ------------------------------
st.write("## 📊 Visualizations")

# Distribution of a column
st.write("### Distribution of Prices")
fig, ax = plt.subplots()
sns.histplot(df['Price'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Countplot for categories
st.write("### Category Count")
fig, ax = plt.subplots()
sns.countplot(x="Category", data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
