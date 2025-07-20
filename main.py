# main.py

from Pricing import black_scholes_call, black_scholes_put
#from Delta import delta_call, delta_put,gamma
import matplotlib.pyplot as plt
import numpy as np
from Pricing import black_scholes_call, black_scholes_put
from Implied_volatility import implied_volatility_call
from Stonks import C_market, X, T, S  # now import S too!

         # Time to expiry (in years)
r = 0.05      # Risk-free interest rate
sigma = 0.2   # Volatility

# Get option prices
call_price = black_scholes_call(S, X, T, r, sigma)
put_price = black_scholes_put(S, X, T, r, sigma)

iv_value = implied_volatility_call(C_market,S,X,T,r)
print("implied_vlotatiltiy",iv_value)


S_values = np.linspace(50, 150, 100)
iv_values = [implied_volatility_call(C_market,S1,X,T,r) for S1 in S_values]
plt.plot(S_values,iv_values)
plt.legend()




'''
# Print results
print(f"Call Price: {call_price:.2f}")
print(f"Put Price: {put_price:.2f}")


# Get Greeks
delta_c = delta_call(S, X, T, r, sigma)
delta_p = delta_put(S, X, T, r, sigma)
gamma_value = gamma(S, X, T, r, sigma)

print(f"Call Delta: {delta_c:.3f}")
print(f"Put Delta: {delta_p:.3f}")
print(f"Gamma:{gamma_value:.3f}")
# Optional: Plot Delta vs S
S_values = np.linspace(50, 150, 100)
deltas_c = [delta_call(s, X, T, r, sigma) for s in S_values]
deltas_p = [delta_put(s, X, T, r, sigma) for s in S_values]
gamma_values=   [gamma(s, X, T, r, sigma) for s in S_values]
plt.plot(S_values, deltas_c, label="Call Delta")
plt.plot(S_values, deltas_p, label="Put Delta")
plt.plot(S_values, gamma_values, label="Gamma")
plt.xlabel("Stock Price (S)")
plt.ylabel("Delta")
plt.title("Delta vs Stock Price")
plt.legend()
plt.grid()
plt.show()
'''