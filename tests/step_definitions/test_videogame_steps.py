import requests
from pytest_bdd import given, when, then, parsers, scenarios
import pytest

# Load all scenarios from the feature file
scenarios("../features/videogame.feature")


@pytest.fixture
def valid_auth_token(base_url):
    auth_url = f"{base_url}/authenticate"
    credentials = {"username": "admin", "password": "admin"}
    response = requests.post(auth_url, json=credentials)
    pytest.auth_response = response

    assert response.status_code == 200
    json_response = response.json()
    assert "token" in json_response
    assert isinstance(json_response["token"], str)
    pytest.auth_token = json_response["token"]

    return pytest.auth_token

@when("I list all videogames")
def list_all_videogames(base_url):
    videogame_url = f"{base_url}/videogame"
    response = requests.get(videogame_url)
    pytest.list_response = response

@then("I should receive a list of videogames")
def verify_list_videogames():
    response = pytest.list_response
    assert response.status_code == 200
    videogames = response.json()
    assert isinstance(videogames, list)
    for videogame in videogames:
        assert "id" in videogame
        assert "name" in videogame
        assert "releaseDate" in videogame
        assert "reviewScore" in videogame
        assert "category" in videogame
        assert "rating" in videogame

@when("I create a new videogame")
def create_videogame(base_url, valid_auth_token_shared):
    create_url = f"{base_url}/videogame"
    headers = {"Authorization": f"Bearer {valid_auth_token_shared}"}
    new_videogame = {
        "category": "Platform",
        "name": "Mario",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }
    response = requests.post(create_url, json=new_videogame, headers=headers)
    pytest.create_response = response

@then("the videogame should be created successfully")
def verify_create_videogame():
    response = pytest.create_response
    assert response.status_code == 200
    created_videogame = response.json()
    assert created_videogame["name"] == "Mario"
    assert created_videogame["category"] == "Platform"
    assert created_videogame["rating"] == "Mature"
    assert created_videogame["releaseDate"] == "2012-05-04"
    assert created_videogame["reviewScore"] == 85

@when(parsers.parse("I get details of the videogame with id {videogame_id}"))
def get_videogame_details(base_url, videogame_id):
    videogame_url = f"{base_url}/videogame/{videogame_id}"
    response = requests.get(videogame_url)
    pytest.get_response = response
@then(parsers.parse('I should see the videogame name "{expected_name}"'))
def verify_videogame_name(expected_name):
    response = pytest.get_response
    assert response.status_code == 200
    videogame = response.json()
    assert videogame["name"] == expected_name

@then("I should receive the details of the videogame")
def verify_get_videogame_details():
    response = pytest.get_response
    assert response.status_code == 200
    videogame = response.json()
    expected_videogame = {
        "id": 3,
        "name": "Tetris",
        "releaseDate": "1984-06-25 23:59:59",
        "reviewScore": 88,
        "category": "Puzzle",
        "rating": "Universal"
    }
    assert videogame == expected_videogame

@given("an existing videogame to update")
def existing_videogame_to_update():
    pytest.existing_videogame_id = 3

@when("I update the videogame")
def update_videogame(base_url, valid_auth_token_shared):
    videogame_id = pytest.existing_videogame_id
    update_url = f"{base_url}/videogame/{videogame_id}"
    headers = {"Authorization": f"Bearer {valid_auth_token_shared}"}
    updated_videogame = {
        "category": "Adventure",
        "name": "Zelda: Breath of the Wild",
        "rating": "Everyone",
        "releaseDate": "2017-03-03",
        "reviewScore": 98
    }
    response = requests.put(update_url, json=updated_videogame, headers=headers)
    pytest.update_response = response

@then("the videogame should be updated successfully")
def verify_update_videogame():
    response = pytest.update_response
    assert response.status_code == 200
    updated_videogame = response.json()
    assert updated_videogame["name"] == "Zelda: Breath of the Wild"
    assert updated_videogame["category"] == "Adventure"
    assert updated_videogame["rating"] == "Everyone"
    assert updated_videogame["releaseDate"] == "2017-03-03"
    assert updated_videogame["reviewScore"] == 98

@when("I get details of the videogame with a non-existent id")
def get_videogame_non_existent_id(base_url):
    non_existent_id = 9999
    videogame_url = f"{base_url}/videogame/{non_existent_id}"
    response = requests.get(videogame_url)
    pytest.non_existent_response = response

@then("I should receive a 404 status code")
def verify_videogame_non_existent_id():
    response = pytest.non_existent_response
    assert response.status_code == 404

@when("I create a new videogame with missing fields")
def create_videogame_missing_fields(base_url, valid_auth_token):
    create_url = f"{base_url}/videogame"
    headers = {"Authorization": f"Bearer {valid_auth_token}"}
    incomplete_videogame = {
        "category": "Platform",
        "name": "Donkey Kong",
        # Missing "rating" and "releaseDate" fields
        "reviewScore": 90
    }
    response = requests.post(create_url, json=incomplete_videogame, headers=headers)
    pytest.missing_fields_response = response

@then("I should receive a 400 status code")
def verify_create_videogame_missing_fields():
    response = pytest.missing_fields_response
    assert response.status_code == 400
