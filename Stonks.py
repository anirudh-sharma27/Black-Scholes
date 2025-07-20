import yfinance as yf
import datetime
ticker = yf.Ticker("AAPL")
S = ticker.history(period="1d")["Close"].iloc[-1]

X = 100       # Strike price
T = 1         # Time to expiry (in years)
r = 0.05      # Risk-free interest rate
sigma = 0.2   # Volatility
option_prices = ticker.history(period="1d")

expires = ticker.options
expiry_date = expires[0]
latest = ticker.option_chain(expiry_date)

call = latest.calls


#at the money means strike and asset price are close

call["diff"] = abs(call["strike"]-S)

#now we get the smallest  diff for atm 
atm_row = call.loc[call["diff"].idxmin()]
X = atm_row["strike"]

#now we get the market option price
C_market = (atm_row['bid'] + atm_row['ask']) / 2  # midpoint

#now we get the expiration date but first we import datetime


today = datetime.date.today()
#IMPORTANT TO GET EXPRIY DATE FROM STOCKS
expiry_dt = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
dates = (expiry_dt-today).days

T = dates/365
print()

__all__ = ["S", "X", "T", "C_market"]
