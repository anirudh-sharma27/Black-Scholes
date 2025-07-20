from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
from pre import load_and_preprocess

def train_and_save_model(model_path="lstm_model.h5"):
    # Load preprocessed data
    X_train, y_train, X_test, y_test, _ = load_and_preprocess()

    model = Sequential()
    model.add(LSTM(units=64, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=32, activation='relu'))
    model.add(Dense(units=1))  # Predicting one value (the next price)

    model.compile(optimizer='adam', loss='mean_squared_error')

    es = EarlyStopping(patience=10, restore_best_weights=True)

    model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test), callbacks=[es])

    # Save the model
    model.save(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()
