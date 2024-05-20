import requests

# Positive Scenario - Valid Login
def test_valid_login():
    url = "https://api.flipkart.com/login"
    payload = {
        "email": "valid_email@example.com",
        "password": "valid_password"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "authentication_token" in response.json()

# Negative Scenario - Invalid Credentials
def test_invalid_login():
    url = "https://api.flipkart.com/login"
    payload = {
        "email": "invalid_email@example.com",
        "password": "invalid_password"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 401

# Negative Scenario - Missing Credentials
def test_missing_credentials():
    url = "https://api.flipkart.com/login"
    payload = {}
    response = requests.post(url, json=payload)
    assert response.status_code == 400

# Performance Testing
# You can use a load testing tool like JMeter or Locust to perform performance testing.
