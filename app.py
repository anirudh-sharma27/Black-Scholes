import streamlit as st
from Pricing import black_scholes_call, black_scholes_put

st.set_page_config(page_title="Option Pricing App", layout="centered")

st.title("📈 Black-Scholes Option Pricing")

st.markdown("Enter the option parameters below:")

# Input fields
S = st.number_input("📊 Stock Price (S)", value=100.0)
X = st.number_input("🎯 Strike Price (X)", value=100.0)
T = st.number_input("⏳ Time to Expiry (Years)", value=1.0, format="%.2f")
r = st.number_input("💰 Risk-Free Rate (r)", value=0.05, format="%.4f")
sigma = st.number_input("📉 Volatility (σ)", value=0.2, format="%.4f")

if st.button("🧮 Calculate Option Prices"):
    call_price = black_scholes_call(S, X, T, r, sigma)
    put_price = black_scholes_put(S, X, T, r, sigma)

    st.success(f"✅ Call Option Price: ${call_price:.2f}")
    st.info(f"📘 Put Option Price: ${put_price:.2f}")
