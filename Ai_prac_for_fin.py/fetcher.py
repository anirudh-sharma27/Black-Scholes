import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


ticker = "AAPL"  
data = yf.download(ticker, start="2020-01-01", end="2024-12-31")


data.to_csv("aapl_data.csv")


plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label="Close Price")
plt.title(f"{ticker} Close Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()
