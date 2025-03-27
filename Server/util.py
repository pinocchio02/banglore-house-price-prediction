import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings("ignore", message="X does not have valid feature names")

__data_columns = None
__locations = None
__model = None

def predict_estimated_price(sqft, location, bhk, bathroom):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bathroom
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    global __data_columns, __locations, __model
    print('Loading saved Artifacts')

    with open('artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('Done loading Artifacts')

load_saved_artifacts()
