import pandas as pd
import plotly.express as px
import streamlit as st

# Set page config
st.set_page_config(page_title="Vehicle Data Dashboard", layout="wide")

# Title and Header
st.title("Interactive Vehicle Data Dashboard")
st.header("Exploratory Analysis of Used Vehicle Listings")

# 🟠 Introduction
with st.expander("📘 Introduction"):
    st.markdown("""
    This dashboard provides an exploratory data analysis (EDA) of a dataset containing listings of used vehicles.
    The goal is to uncover patterns and trends in vehicle pricing, mileage, and other attributes.
    
    **Key questions explored:**
    - What is the distribution of vehicle prices?
    - How do price and odometer readings relate?
    - How does vehicle condition influence price?
    - Which vehicle models have the highest average prices?

    Use the interactive tools below to explore the dataset.
    """)

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

# Show Data Preview
if st.checkbox("Show raw data"):
    st.subheader("Raw Data Preview")
    st.dataframe(df.head(), use_container_width=True)

# Histogram Section
st.subheader("Histogram")
hist_col = st.selectbox("Select column for histogram", df.select_dtypes(include='number').columns)
hist_fig = px.histogram(df, x=hist_col, nbins=50, title=f"Histogram of {hist_col}")
st.plotly_chart(hist_fig, use_container_width=True)

# 🟡 Intermediate Conclusion: Histogram
st.markdown(f"**Observation:** The distribution of `{hist_col}` reveals key insights about its spread and concentration. Look for peaks, skewness, or outliers.")

# Scatter Plot Section
st.subheader("Scatter Plot")
num_cols = df.select_dtypes(include='number').columns
x_col = st.selectbox("Select X-axis", num_cols, key='scatter_x')
y_col = st.selectbox("Select Y-axis", num_cols, key='scatter_y')
scatter_fig = px.scatter(df, x=x_col, y=y_col, color='condition', title=f"{x_col} vs {y_col} by Condition")
st.plotly_chart(scatter_fig, use_container_width=True)

# 🟡 Intermediate Conclusion: Scatter Plot
st.markdown(f"**Observation:** There is a visual relationship between `{x_col}` and `{y_col}`, influenced by vehicle condition. This can help infer how usage affects price.")

# Toggle chart titles
if st.checkbox("Hide chart titles"):
    hist_fig.update_layout(title=None)
    scatter_fig.update_layout(title=None)
    st.plotly_chart(hist_fig, use_container_width=True)
    st.plotly_chart(scatter_fig, use_container_width=True)

# Final Conclusion Section
with st.expander("📌 Final Conclusion"):
    st.markdown("""
    The analysis shows:
    - Vehicle prices vary widely, with notable peaks in certain price ranges.
    - Odometer readings correlate with price; higher mileage often results in lower prices.
    - Condition significantly influences the price; better condition vehicles command higher values.
    - Some models consistently have higher average prices, making them premium in the used vehicle market.

    **Next Steps:** Consider further analysis by integrating time-based trends or regional data for more comprehensive insights.
    """)

# Footer
st.markdown("---")
st.caption("Made with Streamlit | Vehicle Data Dashboard")
