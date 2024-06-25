import requests
import pytest
from pytest_bdd import scenarios, scenario, given, when, then


# Load all scenarios from the feature file
scenarios("../features/authentication.feature")

@pytest.fixture
def api_url():
    return "https://videogamedb.uk/api"


@when("I authenticate with valid credentials")
def authenticate_with_valid_credentials(api_url):
    auth_url = f"{api_url}/authenticate"
    credentials = {"username": "admin", "password": "admin"}
    response = requests.post(auth_url, json=credentials)
    pytest.auth_response = response

@then("I should receive a valid authentication token")
def verify_auth_token():
    response = pytest.auth_response
    assert response.status_code == 200
    json_response = response.json()
    assert "token" in json_response
    assert isinstance(json_response["token"], str)
    pytest.auth_token = json_response["token"]
