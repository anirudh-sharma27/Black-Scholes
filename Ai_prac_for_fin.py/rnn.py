#small predictor 
import numpy as np


# X = list of input sequences
# y = expected next number

a = [
    [2, 4, 6, 8],        # AP (+2)
    [5, 10, 15, 20],     # AP (+5)
    [3, 6, 12, 24],      # GP (×2, approx)
    [2, 4, 8, 16],       # GP (×2)
    [1, 4, 9, 16],       # Squares
    [4, 9, 16, 25],      # Squares
    [3, 9, 27, 81],      # Cubes
    [1, 8, 27, 64],      # Cubes
    [2, 3, 5, 8],        # Fibonacci-ish
    [0, 1, 1, 2],        # Fibonacci
    [11, 22, 33, 44],    # AP (+11)
    [10, 100, 1000, 10000],  # GP (×10)
    [7, 14, 28, 56],     # GP (×2)
    [1, 2, 3, 4],        # AP (+1)
    [5, 25, 125, 625],   # GP (×5)
    [0,0.5,0.707106781,0.866]
]

b = [
    10,    
    25,
    48,
    32,
    25,
    36,
    243,
    125,
    13,
    3,
    55,
    100000,
    112,
    5,
    3125,
    1
]


x = np.array(a,dtype=np.float32)
y = np.array(b,dtype=np.float32)

x = x.reshape((x.shape[0], x.shape[1], 1))

print(x.shape)

#now we wil layout the basic for rnn

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.losses import MeanSquaredError

model = Sequential()
model.add(LSTM(units=128, activation='relu', return_sequences=True, input_shape=(x.shape[1], 1)))
model.add(LSTM(units=64, activation='elu', return_sequences=False))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=1))

#for a model with 50 units and 1 output value

model.compile(optimizer='adam', loss=MeanSquaredError())
#adam is adaptive moment estimation and is generally good for most problems

model.fit(x, y, epochs=1200, verbose=1)
#epoch means no. of times it goes thorugh the data
#verbose has different meanings per value
#0 mean no output seen,1 means progress bar and 2 means one line per epoch
y_pred = model.predict(x, verbose=2)

print("Predicted:", y_pred.flatten())
print("Actual:", y)



rounded_preds = np.round(y_pred.flatten())

# Pretty table
print(f"{'Input Sequence':<25} {'Predicted':<10} {'Actual'}")
print("-" * 50)
for i, seq in enumerate(a):
    print(f"{str(seq):<25} {int(rounded_preds[i]):<10} {int(b[i])}")



from model import save
save(model)



