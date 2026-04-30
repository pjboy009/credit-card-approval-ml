from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open("credit_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

    # Convert to DataFrame
    input_data = pd.DataFrame([list(data.values())], columns=data.keys())
    input_data = input_data.astype(float)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    result = "Approved ✅" if prediction == 1 else "Rejected ❌"
    chance = round(max(probability) * 100, 2)
    
    importances = model.feature_importances_
    features = input_data.columns


    indices = importances.argsort()[-3:][::-1]
    top_features = [features[i] for i in indices]


    return render_template(
      "result.html",
      result=result,
      chance=chance,
      reasons=top_features
)

if __name__ == "__main__":
    app.run(debug=True)