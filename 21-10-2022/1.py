import pickle
import pandas as pd

with open('model.pk', 'rb') as model_file:
    model = pickle.load(model_file)

# model = pickle.load(open("model.pk", 'rb'))

input_df = pd.DataFrame([[54600, 51004]], columns=["Marketing", 'RnD'])

prediction = model.predict(input_df)
print(prediction[0])
