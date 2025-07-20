import numpy as np
import math
from scipy.stats import norm


#sample values


def black_scholes_call(S,X,T,r,sigma):
    d1 = (np.log(S/X) + (r + (sigma**2)/2)*T)/(sigma *(T**0.5))

    d2 = (np.log(S/X) + (r - (sigma**2)/2)*T)/(sigma *(T**0.5))

    C = S*(norm.cdf(d1)) - X*(math.exp(-r*T))*(norm.cdf(d2))
    return C

def black_scholes_put(S,X,T,r,sigma):
    d1 = (np.log(S/X) + (r + (sigma**2)/2)*T)/(sigma *(T**0.5))

    d2 = (np.log(S/X) + (r - (sigma**2)/2)*T)/(sigma *(T**0.5))

    P = X*(math.exp(-r*T))*(norm.cdf(-d2)) - S*(norm.cdf(-d1))
    return P