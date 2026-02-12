import joblib
import pandas as pd
import os
model_filename = 'autism_model.pkl'
if not os.path.exists(model_filename):
    print(f" Error: The file '{model_filename}' was not found.")
    print(" Please run 'train_model.py' first.")
else:
    print(f"Loading AI Model from '{model_filename}'...")
    model = joblib.load(model_filename)
    print("AI Model loaded successfully!\n")

    print("--- AI Autism Screening Test ---")
 
    child_data = {
        'A1': [0],
        'A2': [0],
        'A3': [0],
        'A4': [0],
        'A5': [0],
        'A6': [0],
        'A7': [0],
        'A8': [0],
        'A9': [0],
        'A10': [0],
        
        'Age': [24],
        'Sex': [1],
        'Jaundice': [0],
        'Family_ASD': [0]
    }

    input_df = pd.DataFrame(child_data)

    prediction = model.predict(input_df)[0]
    
    probability = model.predict_proba(input_df)[0]
    print("\n---------------------------------------------------")
    print(f"🔍 ANALYZING DATA FOR AGE: {child_data['Age'][0]} months...")
    print("---------------------------------------------------")
    
    if prediction == 1:
        confidence = probability[1] * 100
        print(f"⚠️  RESULT: HIGH RISK of ASD Detected")
        print(f"📊 Confidence: {confidence:.2f}%")
        print("   Recommendation: Please consult a specialist.")
    else:
        confidence = probability[0] * 100
        print(f"✅ RESULT: Low Risk (Healthy)")
        print(f"📊 Confidence: {confidence:.2f}%")
        print("   Recommendation: Standard developmental monitoring.")
    print("---------------------------------------------------\n")