import requests
import json

url = 'http://127.0.0.1:5000/predict' 

data = {
    "A1": 1, "A2": 0, "A3": 1, "A4": 0, "A5": 1,
    "A6": 0, "A7": 1, "A8": 1, "A9": 0, "A10": 1,
    "Age": 24, "Sex": 1, "Jaundice": 0, "Family_ASD": 1
}

try:
    response = requests.post(url, json=data)
    print(" Status Code:", response.status_code)
    print("\n JSON Response from Server:")
    print(json.dumps(response.json(), indent=4))
except Exception as e:
    print(" Error:", e)