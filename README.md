# sprint 4
 Car data science project


# 🚗 Vehicle Data Analysis Dashboard
This repository contains an exploratory data analysis (EDA) of a used vehicles dataset, along with an interactive Streamlit dashboard for visualizing vehicle data. The project allows users to explore relationships between vehicle features such as price, odometer reading, and condition through dynamic charts.

# 📂 Contents
EDA.ipynb — Jupyter Notebook with in-depth data cleaning, exploration, and visualizations.

app.py — Streamlit app for interactive data exploration.

vehicles_us.csv — Dataset of used vehicles in the U.S.

requirements.txt — Required Python packages for the project.

# 📊 Features
Data cleaning and preprocessing (e.g., handling missing values, ensuring correct data types).

Histograms of vehicle price and odometer readings.

Scatter plot: Odometer vs. Price colored by condition.

Bar chart: Average Price by Model.

Interactive controls in Streamlit (checkboxes, dropdowns for column selection).

# 🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/vehicle-data-dashboard.git
cd vehicle-data-dashboard

2. Install Dependencies
Create a virtual environment (optional but recommended), then install the required packages:
bash
Copy
Edit
pip install -r requirements.txt
Note: Only pandas, plotly, and streamlit are used in this project.

🧪 Running the Jupyter Notebook
To explore the EDA in the notebook:

bash
Copy
Edit
jupyter notebook EDA.ipynb
Use this to explore summary statistics, visualize trends, and verify data cleaning steps.

# 📈 Running the Streamlit Dashboard
Start the Streamlit app in your terminal:

bash
Copy
Edit
streamlit run app.py
This will open the dashboard in your default web browser at http://localhost:8501.

# 📌 Requirements
All dependencies are listed in requirements.txt:
txt
Copy
Edit
pandas==2.0.3
plotly==5.15.0
streamlit==1.25.0



