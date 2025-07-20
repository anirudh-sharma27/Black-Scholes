import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess(filename="aapl_data.csv", window_size=5, train_split=0.8):
    # Load CSV
    df = pd.read_csv(filename)

    # Fix: Ensure only numeric 'Close' values
    if "Close" not in df.columns:
        print("Available columns:", df.columns)
        raise ValueError("No 'Close' column found in the dataset!")

    df = df.dropna(subset=["Close"])  # drop NaNs
    df["Close"] = pd.to_numeric(df["Close"], errors='coerce')  # force numeric
    df = df.dropna(subset=["Close"])  # drop any conversion errors again

    prices = df["Close"].values.reshape(-1, 1)

    # Normalize
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    # Sequence creation
    X, y = [], []
    for i in range(window_size, len(scaled)):
        X.append(scaled[i - window_size:i])
        y.append(scaled[i])

    X, y = np.array(X), np.array(y)

    # Train/test split
    split = int(train_split * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    return X_train, y_train, X_test, y_test, scaler
if __name__ == "__main__":
    X_train, y_train, X_test, y_test, scaler = load_and_preprocess()
    print("Shapes:", X_train.shape, y_train.shape)
