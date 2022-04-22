import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Finance Dashboard')

tickers = ('AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TWTR', 'BTC-USD', 'ETH-USD', 'NVA.TO', 'SUGR.V')

dropdown = st.multiselect('Select Stock', tickers)

start = st.date_input('Start Date', value= pd.to_datetime('2020-01-01'))
end = st.date_input('End Date', value= pd.to_datetime('2022-05-01'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    # df = yf.download(dropdown, start, end)['Adj Close']
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    