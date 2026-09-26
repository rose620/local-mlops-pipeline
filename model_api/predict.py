import json
import requests

url = "http://localhost:8000/predict"
payload_path = "sample_payload.json"

print("🚀 Sending sample payload via Python requests...")

try:
    with open(payload_path, "r") as f:
        payload = json.load(f)
        
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    print("🎯 Prediction Response:")
    print(json.dumps(response.json(), indent=2))

except Exception as e:
    print(f"❌ Error: {e}")
    print("Ensure your Docker container is running locally on port 8000.")
