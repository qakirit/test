import pytest
import requests

# Define the URL of your application
BASE_URL = "https://practicetestautomation.com/practice-test-login/"


# Test Registration
def test_registration():
    # Test data for registration
    data = {
        "Username": "student",
        "Password": "Password123"  # Fixed formatting
        # Add other required fields for registration
    }

    response = requests.post(f"{BASE_URL}/register", json=data)
    assert response.status_code == 200  # Assuming 200 is success for registration

    # Assuming your application returns some data upon registration, you can validate it here
    response_data = response.json()
    assert "message" in response_data
    assert response_data["message"] == "Congratulations student. You successfully logged in!"


if __name__ == "__main__":
    pytest.main()
