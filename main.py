import streamlit as st
import pandas as pd
import yfinance as yf

#build an app stock
# the # is used to make a header
# Takes users desire ticket symbol and presents it in a graph using streamlit web

st.write( """

# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

title = st.text_input('Enter Ticket Symbol', 'Ticket')
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(title)

tickerDf = tickerData.history(period='1d', start= '2010-5-31', end='2023-3-15')

st.write("""
## Closing Chart 
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Chart
""")
st.line_chart(tickerDf.Volume)



