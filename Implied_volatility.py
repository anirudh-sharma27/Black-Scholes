from Pricing import black_scholes_call,black_scholes_put
#root finder is brentq
from scipy.optimize import brentq
from Stonks import C_market

def implied_volatility_call(C_market,S,X,T,r):
    def diff(sigma):
        price = black_scholes_call(S,X,T,r,sigma)
        return price-C_market
    #root withing range of 0.0001 and 5
    iv = brentq(diff,.0001,5.0)
    return iv

