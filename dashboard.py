
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

sns.set(style='dark')

# Load data
df = pd.read_csv('main_data.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Sidebar
st.sidebar.header(' Filter Data')
min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()
start_date, end_date = st.sidebar.date_input('Rentang Waktu', [min_date, max_date])

# Filter
main_df = df[(df['order_purchase_timestamp'].dt.date >= start_date) & 
             (df['order_purchase_timestamp'].dt.date <= end_date)]

st.title(' E-Commerce Dashboard')

# Review Score
st.subheader(' Review Score Distribution')
fig, ax = plt.subplots(figsize=(10, 5))
main_df['review_score'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
st.pyplot(fig)

# Top Categories
st.subheader(' Top 10 Product Categories')
fig, ax = plt.subplots(figsize=(10, 5))
main_df['product_category_name_english'].value_counts().head(10).plot(kind='barh', color='lightcoral', ax=ax)
st.pyplot(fig)

# Payment Methods
st.subheader(' Payment Methods')
fig, ax = plt.subplots(figsize=(6, 6))
main_df['payment_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
st.pyplot(fig)

# Price Statistics
st.subheader(' Price Statistics')
col1, col2, col3, col4 = st.columns(4)
col1.metric('Mean', f"${main_df['price'].mean():.2f}")
col2.metric('Median', f"${main_df['price'].median():.2f}")
col3.metric('Min', f"${main_df['price'].min():.2f}")
col4.metric('Max', f"${main_df['price'].max():.2f}")

st.caption('Copyright © 2024')
