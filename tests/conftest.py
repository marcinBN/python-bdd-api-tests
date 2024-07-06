import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Description of the env option.")

@pytest.fixture(scope='session')
def base_url(request):
    env = request.config.getoption('--env')
    if env == 'dev':
        return "https://videogamedb.uk.dev/api"
    elif env == 'prod':
        return "https://videogamedb.uk/api"
    else:
        raise ValueError(f"Unknown environment '{env}'. Please use '--env dev' or '--env prod'.")

@pytest.fixture(scope="session")
def valid_auth_token_shared(base_url):
    auth_url = f"{base_url}/authenticate"
    credentials = {"username": "admin", "password": "admin"}
    response = requests.post(auth_url, json=credentials)
    assert response.status_code == 200
    json_response = response.json()
    assert "token" in json_response

    pytest.auth_token = json_response["token"]
    return json_response["token"]