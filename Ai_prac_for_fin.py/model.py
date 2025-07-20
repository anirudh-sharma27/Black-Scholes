from tensorflow.keras.models import load_model

def save(model, path='sequence_model.h5'):
    model.save(path)
    print(f"Model saved to {path}")

def load(path='sequence_model.h5'):
    model = load_model(path)
    print(f" Model loaded from {path}")
    return model
