# app.py - Streamlit Dashboard for Vehicle Data

import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px

# Title and Header
st.title("Interactive Data Dashboard")
st.header("Exploratory Analysis of Your Dataset")

# Load Data
df = pd.read_csv('vehicles_us.csv')   # Adjust path if needed

# Show Data Preview
if st.checkbox("Show raw data"):
    st.write(df.head())

# Plotly Histogram
st.subheader("Histogram")
selected_hist_col = st.selectbox("Select column for histogram", df.select_dtypes(include='number').columns)
hist_fig = px.histogram(df, x=selected_hist_col, title=f"Histogram of {selected_hist_col}")
st.plotly_chart(hist_fig)

# Plotly Scatter Plot
st.subheader("Scatter Plot")
numeric_cols = df.select_dtypes(include='number').columns
x_col = st.selectbox("Select X-axis", numeric_cols, key='scatter_x')
y_col = st.selectbox("Select Y-axis", numeric_cols, key='scatter_y')

scatter_fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot: {x_col} vs {y_col}")
st.plotly_chart(scatter_fig)

# Checkbox to toggle title visibility
if st.checkbox("Hide chart titles"):
    hist_fig.update_layout(title=None)
    scatter_fig.update_layout(title=None)
    st.plotly_chart(hist_fig)
    st.plotly_chart(scatter_fig)
