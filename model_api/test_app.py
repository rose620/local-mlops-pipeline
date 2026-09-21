from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    # Mock Data layout matching dataset schema
    mock_payload = {
        "fixed_acidity": 7.4,
        "volatile_acidity": 0.70,
        "citric_acid": 0.00,
        "residual_sugar": 1.9,
        "chlorides": 0.076,
        "free_sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4
    }
    
    # Send mock POST request to container's API endpoint
    response = client.post("/predict", json=mock_payload)
    
    # Assertions to ensure code executes properly
    assert response.status_code == 200
    assert "predicted_quality" in response.json()
