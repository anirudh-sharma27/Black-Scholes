from Pricing import black_scholes_call, black_scholes_put
import matplotlib.pyplot as plt
import numpy as np

X = 100       # Strike price (e.g., $100)
T = 1         # Time to maturity in years (e.g., 1 year)
r = 0.05

plt.xlabel('Stock Price (S)')
plt.ylabel('Call Option Price (C)')

S_values = np.linspace(50, 150, 100)
sigma_values = [0.1, 0.2, 0.3,0.4,0.50,0.6,0.7,0.8]
for sigma in sigma_values:
    call_prices =([black_scholes_call(S1,X,T,r,sigma) for S1 in S_values])
    plt.plot(S_values, call_prices, label=f"σ = {sigma:.1f}")
    

plt.legend()
plt.show()

