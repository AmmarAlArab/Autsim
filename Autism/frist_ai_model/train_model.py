import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

input_file = 'autism_data_clean.csv'
model_file = 'autism_model.pkl'

if not os.path.exists(input_file):
    print(f"❌ Error: {input_file} not found. Please run clean_data.py first.")
else:
    print("🔄 Loading clean dataset...")
    df = pd.read_csv(input_file)
    
    X = df.drop('Class', axis=1)
    
    y = df['Class']
    
    print(f"✅ Data prepared: {X.shape[0]} samples.")

    print("✂️  Splitting data into Training and Testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("🧠 Training the AI model... (Teaching it patterns)")
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    model.fit(X_train, y_train)
    
    print("✅ Training complete!")

    print("📝 Testing the model on unseen data...")
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f"\n🎯 Model Accuracy: {accuracy * 100:.2f}%")
    
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, predictions))
    
    joblib.dump(model, model_file)
    print(f"\n💾 Intelligence saved to file: '{model_file}'")
    print("You can now take this .pkl file to your Backend API!")