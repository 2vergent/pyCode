import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#get date for exactly on year before
day = str(pd.to_datetime('today').strftime('%Y-%m-%d'))
one_year = int(day[0:4]) - 1
one_year = str(one_year) + day[len(day)-6: len(day)]

#stock = input("Enter Stock Symbol: ")

#exporting the stock historical data to a CSV file
stock_df = yf.download("HDFCBANK.NS", start = one_year, end = day)
stock_df.to_csv('stock.csv')

#reading CSV file and getting Adjusted Close values and dates
df = pd.read_csv('stock.csv')
adj_close = df['Adj Close'].tolist()
dates = df['Date'].tolist()

#calculating and plotting Short term group Exponential Moving Average for Adjusted close values
for x in [3, 5, 8, 10, 12, 15]:
    ema = df['Adj Close'].ewm(span=x, adjust=False).mean()
    plt.plot(dates, ema, "r")

#calculating and plotting Long term group Exponential Moving Average for Adjusted close values
for x in [30, 35, 40, 45, 50, 60]:
    ema = df['Adj Close'].ewm(span=x, adjust=False).mean()
    plt.plot(dates, ema, "g")

#plotting adjusted close values
plt.plot(dates, adj_close, "b")

plt.show()