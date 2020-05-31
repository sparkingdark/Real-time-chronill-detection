import numpy as np
import pickle


model = pickle.load(open('models/model.sav', 'rb'))

print(model.predict([[0.88,0.65,0.94]]))