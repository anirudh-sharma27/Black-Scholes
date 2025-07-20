import yfinance as yf

ticker = yf.Ticker("AAPL")

data = ticker.history(period="1y")
stock_price = data["Close"].iloc[-1]  # Get the last closing price

print(data.head())
#till here is the step to fetch data from yahoo finance

expires= ticker.options
print("Available expiration dates:", expires)
#shows expiration dates for options]

option_chain = ticker.option_chain(expires[0])

calls= option_chain.calls
put = option_chain.puts

print(calls,put)
#shows many different options from the nearest expiration date
 
nearest_call = calls.iloc[10]  # or use logic to pick ATM option

strike_price = nearest_call['strike']
market_price = nearest_call['lastPrice']

print(f"Strike: {strike_price}, Market Option Price: {market_price}")
