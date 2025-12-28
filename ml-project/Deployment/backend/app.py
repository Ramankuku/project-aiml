from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load your model
# model = joblib.load("RandomForest.joblib")


@app.route("/")
def home():
    return "Flask server is running!"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  

        df = pd.DataFrame([{
            "Customer Type": data["Customer Type"],
            "Age": data["Age"],
            "Type of Travel": data["Type of Travel"],
            "Class": data["Class"],
            "Flight Distance": data["Flight Distance"],
            "Flight Service": data["Flight Service"],
            "Total_delayed": data["Total_delayed"],
            "Online Services": data["Online Services"]
        }])

        # Make prediction
        # prediction_proba = model.predict_proba(df)[0][1]  
        # prediction_label = model.predict(df)[0] 

        return jsonify({
            "prediction": int(prediction_label),
            "probability": float(prediction_proba)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
