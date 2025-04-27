# app.py

import yfinance as yf
import pandas as pd
import datetime
import streamlit as st

# =========================
# 1. Get AAPL Stock Data
# =========================
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=5*365)  # Last 5 years

df = yf.download('AAPL', start=start_date, end=end_date)

# Flatten multi-level column names if present
df.columns = df.columns.get_level_values(0)

# Reset index to make 'Date' a column
df.reset_index(inplace=True)

# =========================
# 2. Filter Data for Current Month
# =========================
# Get the current year and month
current_year = end_date.year
current_month = end_date.month

# Filter data for the current month
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

df_current_month = df[(df['Year'] == current_year) &
                      (df['Month'] == current_month)]

# =========================
# 3. Streamlit UI Layout
# =========================
st.title('AAPL Closing Price - This Month')

# For the line chart, we only need the Date and Close columns
df_current_month_plot = df_current_month[['Date', 'Close']]

# Display a line chart using Streamlit's line_chart method
st.line_chart(df_current_month_plot.set_index('Date'))
