# greeks.py

from scipy.stats import norm
import numpy as np

def d1(S, X, T, r, sigma):
    return (np.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def delta_call(S, X, T, r, sigma):
    d_1 = d1(S, X, T, r, sigma)
    return norm.cdf(d_1)

def delta_put(S, X, T, r, sigma):
    d_1 = d1(S, X, T, r, sigma)
    return norm.cdf(d_1) - 1

def gamma(S, X, T, r, sigma):
    d_1 = d1(S,X,T,r,sigma)
    return norm.pdf(d_1) / (S * sigma * np.sqrt(T))