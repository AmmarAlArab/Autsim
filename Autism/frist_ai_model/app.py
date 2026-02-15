from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
import sys

app = Flask(__name__)
CORS(app)

model_file = 'autism_model.pkl'
model = None

if os.path.exists(model_file):
    model = joblib.load(model_file)
    print("Model loaded")
else:
    print("Model not found")
    sys.exit(1)

@app.route('/', methods=['GET'])
def home():
    return "<h1> Autism API is Running!</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    global model
    try:
        data = request.get_json()
        
        required_columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 
                            'Age', 'Sex', 'Jaundice', 'Family_ASD']
        input_df = pd.DataFrame([data])[required_columns]

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]
        confidence = float(probability[prediction])

        social_score = (data['A1'] + data['A4'] + data['A5'] + data['A7']) / 4.0
        comm_score = (data['A2'] + data['A3'] + data['A6'] + data['A9']) / 4.0
        repetitive_score = (data['A8'] + data['A10']) / 2.0

        def get_level(score):
            if score <= 0.3: return "Low"
            elif score <= 0.6: return "Moderate"
            else: return "High"

        result = {
            'status': 'success',
            'final_result': 'Autism Traits Detected' if prediction == 1 else 'No Clear Traits',
            'risk_level': get_level(confidence if prediction == 1 else 1-confidence),
            
            'details': {
                'social': {
                    'score': round(social_score * 100, 1),
                    'level': get_level(social_score)
                },
                'communication': {
                    'score': round(comm_score * 100, 1),
                    'level': get_level(comm_score)
                },
                'repetitive': {
                    'score': round(repetitive_score * 100, 1),
                    'level': get_level(repetitive_score)
                }
            }
        }

        print(f"[RESPONSE] Sent detailed analysis.")
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)