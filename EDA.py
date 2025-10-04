import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="EDA App", layout="wide")

st.title("📊 E-commerce Dataset EDA")

# File uploader
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success("✅ Dataset loaded successfully!")
    st.write("Shape:", df.shape)

    st.subheader("👀 Preview")
    st.dataframe(df.head())

    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    cat_cols = df.select_dtypes(include=['object','category']).columns.tolist()
    if cat_cols:
        st.write("Sample categorical distributions:")
        for c in cat_cols[:3]:
            st.write(f"Value counts for {c}:")
            st.bar_chart(df[c].value_counts().head(10))

    # Correlation
    num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    if len(num_cols) >= 2:
        st.subheader("🔗 Correlation Heatmap")
        corr = df[num_cols].corr()
        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
        st.pyplot(fig)

    # Interactive scatter
    if 'category' in df.columns and len(num_cols) >= 2:
        st.subheader("🎨 Scatter by Category")
        fig = px.scatter(df, x=num_cols[0], y=num_cols[1], color='category')
        st.plotly_chart(fig)
