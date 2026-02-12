from sklearn.ensemble import RandomForestClassifier

print("--- Building Model Structure ---")

number_of_trees = 100

print(f"Algorithm Selected: Random Forest Classifier")
print(f"Number of Decision Trees: {number_of_trees}")

model = RandomForestClassifier(n_estimators=number_of_trees, random_state=42)

print("\n Model Object Created Successfully!")
print(model)
print("\n---------------------------------")
print("The model structure is built. It is an 'Empty Brain' ready to receive data for training.")