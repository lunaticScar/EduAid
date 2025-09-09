import joblib
import numpy as np

model = joblib.load(r"C:\Users\awast\Downloads\student_model2.pkl")

sample = np.array([1,	6	,1	,1	,1	,3	,4	,4	,1,	0,0,0,0	,19	,6	,6,	14.000000,	6	,6,	13.666667]).reshape(1, -1)

prediction = model.predict(sample)
print("Prediction:", prediction[0])
