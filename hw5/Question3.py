import pickle
import sklearn 

with open("model1.bin", 'rb') as file:
  model = pickle.load(file)
  dv = pickle
with open("dv.bin", 'rb') as file:
  dv = pickle.load(file)


client = {"job": "retired", "duration": 445, "poutcome": "success"}
#client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
#model.predict(dv.transform([client]))
result = model.predict_proba(dv.transform([client]))[0,1]

print(result) #0.9019309332297606

