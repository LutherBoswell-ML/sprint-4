# app.py - Streamlit Dashboard for Vehicle Data
import pandas as pd
import plotly.express as px
import streamlit as st

# Set page config
st.set_page_config(page_title="Vehicle Data Dashboard", layout="wide")

# Title and Header
st.title("Interactive Data Dashboard")
st.header("Exploratory Analysis of Your Vehicle Dataset")

# Load Data
df = pd.read_csv('vehicles_us.csv')

# Clean numeric columns
for col in df.select_dtypes(include='number').columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Clean object columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str)

# Clean boolean columns
for col in df.select_dtypes(include='bool').columns:
    df[col] = df[col].astype(str)

# Show Data Preview safely
if st.checkbox("Show raw data"):
    st.subheader("Raw Data Preview")
    st.dataframe(df.head(), use_container_width=True)

# Plotly Histogram
st.subheader("Histogram")
hist_col = st.selectbox("Select column for histogram", df.select_dtypes(include='number').columns)
hist_fig = px.histogram(df, x=hist_col, nbins=50, title=f"Histogram of {hist_col}")
st.plotly_chart(hist_fig, use_container_width=True)

# Plotly Scatter Plot
st.subheader("Scatter Plot")
num_cols = df.select_dtypes(include='number').columns
x_col = st.selectbox("Select X-axis", num_cols, key='scatter_x')
y_col = st.selectbox("Select Y-axis", num_cols, key='scatter_y')
scatter_fig = px.scatter(df, x=x_col, y=y_col, color='condition', title=f"{x_col} vs {y_col} by Condition")
st.plotly_chart(scatter_fig, use_container_width=True)

# Toggle chart titles
if st.checkbox("Hide chart titles"):
    hist_fig.update_layout(title=None)
    scatter_fig.update_layout(title=None)
    st.plotly_chart(hist_fig, use_container_width=True)
    st.plotly_chart(scatter_fig, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Made with Streamlit | Vehicle Data Dashboard")
