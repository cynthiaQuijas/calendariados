import json
import joblib
import numpy as np
import pandas as pd
import sklearn
from azureml.core.model import Model

def init():
    # Load model using joblibs
    global loaded_model
    model_path = Model.get_model_path('modelo_random_forest_reg')
    loaded_model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)['data'][0]
    data = pd.DataFrame(data)

    result = loaded_model.predict(data).tolist()

    return json.dumps(result)
