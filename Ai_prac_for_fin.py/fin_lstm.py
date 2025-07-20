from model import load
model = load()
import pandas as pd

#y_pred = model.predict(x, verbose=0)
#print("Predicted:", y_pred.flatten())
import yfinance as yf

ticker = yf.Ticker("AAPL")

data = ticker.history(period="1y")
stock_price = data["Close"]
print(type(stock_price))