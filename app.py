# app.py

import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objs as go
import streamlit as st

# =========================
# 1. Get AAPL Stock Data
# =========================
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=5*365)  # Last 5 years

df = yf.download('AAPL', start=start_date, end=end_date)

# Reset index to make 'Date' a column
df.reset_index(inplace=True)

# =========================
# 2. Streamlit UI Layout
# =========================
st.title('📈 AAPL Closing Price - Last 5 Years')

# Add a line chart using Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Close'],
    mode='lines',
    name='AAPL Close Price'
))

fig.update_layout(
    title='AAPL Closing Price Over Time',
    xaxis={'title': 'Date'},
    yaxis={'title': 'Close Price (USD)'},
    hovermode='closest'
)

st.plotly_chart(fig)
