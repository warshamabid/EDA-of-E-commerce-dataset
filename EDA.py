import streamlit as st
#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

# Set style for plots
sns.set(style='whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


# Load dataset 
df = pd.read_csv("C:\\Users\\Warsham\\Downloads\\ecommerce_dataset.csv")

print("✅ Dataset loaded successfully!")
print("Shape of dataset:", df.shape)

# Display first 7 rows
df.head(7)


# In[11]:


# Summary statistics for numeric columns
print("--- Numeric summary ---")
display(df.describe().T)

# For categorical columns: show top value counts
cat_cols = df.select_dtypes(include=['object','category']).columns.tolist()
if len(cat_cols) > 0:
    print("\n--- Categorical columns sample value counts ---")
    for c in cat_cols[:3]:
        print(f"\nValue counts for {c}:")
        print(df[c].value_counts().head(10))


# In[12]:


# Correlation matrix (numeric features) and heatmap
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()

if len(num_cols) >= 2:
    corr = df[num_cols].corr()
    print("Correlation matrix:")
    display(corr)

    plt.figure(figsize=(10,6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap of Numeric Features")
    plt.show()
else:
    print("Not enough numeric columns for correlation heatmap.")


# In[16]:


# Grouped statistics by 'category' column
if 'category' in df.columns:
    # only numeric columns for aggregation
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    print("Grouping by 'category' and computing mean and std for numeric columns:\n")
    display(df.groupby('category')[numeric_cols].mean().T)
    display(df.groupby('category')[numeric_cols].std().T)

    print("\nCounts per group:")
    print(df['category'].value_counts())
else:
    print("No 'category' column found for grouping.")


# In[23]:


# Select numeric columns and remove "order_id"
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
num_cols = [c for c in num_cols if c.lower() != "order_id"]   # exclude order_id

if len(num_cols) > 0:
    colors = plt.cm.tab20.colors  

    # Histograms
    for i, col in enumerate(num_cols):
        data = df[col].dropna()
        if data.nunique() > 1:   # skip constant/empty
            plt.figure(figsize=(6,4))
            plt.hist(data, bins=20, color=colors[i % len(colors)], edgecolor='black')
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"⚠️ Skipped histogram for '{col}' (constant/empty values)")

    # Boxplots
    for i, col in enumerate(num_cols):
        data = df[col].dropna()
        if data.nunique() > 1:
            plt.figure(figsize=(4,5))
            sns.boxplot(y=data, color=colors[i % len(colors)])
            plt.title(f"Boxplot of {col}")
            plt.show()
        else:
            print(f"⚠️ Skipped boxplot for '{col}' (constant/empty values)")
else:
    print("No numeric columns to plot.")


# In[24]:


# Interactive plots by category
if 'category' in df.columns:
    num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    if len(num_cols) >= 2:
        fig = px.scatter(df, x=num_cols[0], y=num_cols[1], color='category',
                         title=f"{num_cols[0]} vs {num_cols[1]} by Category")
        fig.show()

        for c in num_cols[:2]:
            fig = px.violin(df, x='category', y=c, box=True, points='all',
                            title=f"Violin plot of {c} by Category")
            fig.show()
    else:
        print("Not enough numeric columns for interactive plots.")


# In[ ]:




