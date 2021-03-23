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
    ema_short = df['Adj Close'].ewm(span=x, adjust=False).mean()
    plt.plot(dates, ema_short, "r")

#calculating and plotting Long term group Exponential Moving Average for Adjusted close values
for x in [30, 35, 40, 45, 50, 60]:
    ema_long = df['Adj Close'].ewm(span=x, adjust=False).mean()
    plt.plot(dates, ema_long, "g")

ema_short3 = df['Adj Close'].ewm(span=3, adjust=False).mean()
plt.plot(dates, ema_short3, "r")
ema_short5 = df['Adj Close'].ewm(span=5, adjust=False).mean()
plt.plot(dates, ema_short5, "r")
ema_short8 = df['Adj Close'].ewm(span=8, adjust=False).mean()
plt.plot(dates, ema_short8, "r")
ema_short10 = df['Adj Close'].ewm(span=10, adjust=False).mean()
plt.plot(dates, ema_short10, "r")
ema_short12 = df['Adj Close'].ewm(span=12, adjust=False).mean()
plt.plot(dates, ema_short12, "r")
ema_short15 = df['Adj Close'].ewm(span=15, adjust=False).mean()
plt.plot(dates, ema_short15, "r")

ema_long30 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long30, "g")
ema_long35 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long35, "g")
ema_long40 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long40, "g")
ema_long45 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long45, "g")
ema_long50 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long50, "g")
ema_long60 = df['Adj Close'].ewm(span=x, adjust=False).mean()
plt.plot(dates, ema_long60, "g")





'''short_start = []
long_start = []

x = 0
while (x < 248):
    short_start.append(ema_short[x])
    long_start.append(ema_long[x])
    x = x + 5'''

#plotting adjusted close values
plt.plot(dates, adj_close, "b")

plt.show()