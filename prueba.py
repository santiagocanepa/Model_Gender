import pickle
from model import feature_extractor,vectorizer




if __name__ == "__main__":
    
    # Cargar el modelo desde el archivo
    with open('./modelo.pkl', 'rb') as f:
        modelo = pickle.load(f)

    # Hacer inferencias con el modelo


    def predict_gender(name):
        features = feature_extractor(name.lower())
        X = vectorizer.transform([features])
        prediction = modelo.predict(X)
        return "hombre" if prediction[0] == 1 else "mujer"

    nueva_prediccion = predict_gender('sofia')
    print(nueva_prediccion)