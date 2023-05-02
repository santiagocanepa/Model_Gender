import warnings
from name_predictor.separetor import possible_name
import pickle

# Guardar el modelo en un archivo


# Desactivar todas las advertencias
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
# Load dataset
data = pd.read_csv('./data/classified_names_augmentation_combined.csv') # Replace with the path to your dataset file
new_row = {'nombre': 'cxmila', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'romina', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'agus', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'juli', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'juan', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'viole', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'caro', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)
new_row = {'nombre': 'rocio', 'gender': 'f'}
data = data.append(new_row, ignore_index=True)



# Preprocess data
data['nombre'] = data['nombre'].str.lower()
data['label'] = data['gender'].apply(lambda x: 1 if x == 'm' else 0) # Convert gender labels to binary format

# Extract features
def feature_extractor(name):
    features = []
    for i, c in enumerate(name):
        features.append(c + str(i))
    return ' '.join(features)
    #features = ''.join(sorted(set(name)))
    #if name[-1] == 'a':  # Check if the name ends with an "a"
    #    features += '#'  # Append a special character to the features string
    #return features


data['features'] = data['nombre'].apply(feature_extractor)
vectorizer = CountVectorizer(analyzer='char', ngram_range=(3, 10))
X = vectorizer.fit_transform(data['features'])
y = data['label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}


# Train a classif
clf = MultinomialNB()
grid_search = GridSearchCV(clf, param_grid, cv=5)

# Perform the grid search
grid_search.fit(X_train, y_train)

# Get the best model
best_clf = grid_search.best_estimator_

# Make predictions
y_pred = best_clf.predict(X_test)


with open('modelo.pkl', 'wb') as f:
    pickle.dump(best_clf, f)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
# Make predictions

print("Accuracy: {:.2f}%".format(accuracy * 100))

# Function to predict gender of a name
def predict_gender(name):
    features = feature_extractor(name.lower())
    X = vectorizer.transform([features])
    prediction = best_clf.predict(X)
    return "hombre" if prediction[0] == 1 else "mujer"

# Example usage
#name = "Felipe"
#print(f"El predictor de genero del nombre:'{name}' es {predict_gender(name)}")
def probs(name):
    features = feature_extractor(name.lower())
    X = vectorizer.transform([features])
    y_pred_proba = best_clf.predict_proba(X)
    y_pred_proba = np.max(y_pred_proba)
    return ("{:.2f}% seguro".format(y_pred_proba * 100))



if __name__ == '__main__':
    test = ['ourdessimonee_','soofi.tejada','lautyy_dj_',
            'celes_garro','agustinaa_michell','rociobh_',
            'lautty_10','romina_viss','catiwillging','sofii._garrido',
            'simon_dragani','lolaa.aguirre','juliminio_','lucreeconte',
            'carolgerth_','sebastian____alexis','luciano_armohaa','fran_santadino',
            'santiago_stegmann','cxmila_01','lucas_acosta_a','melinacacereees',
            'zoecarolinah','cande.rodriguez25','carlupereyra_','lugalante_','guadajaimee',
            'eli.matta_','agusquintana_','stefanodiferna','belu.darco',
            'jaaazruiz','katriel.94','marttuleiva','candela_rams','jula.curubeto','vane_qac',
            'rocioalcaraz_','__zoee3','franciscor.me','rrenataromero']



    for i in test:
        name_short = possible_name(i)
        print(f"El predictor de genero del nombre: '{i}' es {predict_gender(name_short)}")


#    while True:
#        name = input("Introduce un nombre para predecir su género (escribe 'salir' para terminar): ")
#        if name.lower() == "salir":
#            break
#        else:
#            name_short = possible_name(name)
#            
#            print(f"El predictor de genero del nombre: '{name_short}' es {predict_gender(name_short)}",
#                  probs(name))
