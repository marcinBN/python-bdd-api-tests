Feature: Videogame API

  @details
  Scenario: List all videogames
    When I list all videogames
    Then I should receive a list of videogames

  @details
  Scenario: Create a new videogame
    When I create a new videogame
    Then the videogame should be created successfully

  @details
  Scenario: Get details of a specific videogame
    When I get details of the videogame with id 3
    Then I should receive the details of the videogame

  @details
  Scenario Outline: Get details of a specific videogame-new
    When I get details of the videogame with id <videogame_id>
    Then I should see the videogame name "<expected_name>"

    Examples:
      | videogame_id | expected_name   |
      | 1            | Resident Evil 4 |
      | 2            | Gran Turismo 3  |

  Scenario: Update a videogame
    Given an existing videogame to update
    When I update the videogame
    Then the videogame should be updated successfully

  Scenario: Delete a videogame
    Given an existing videogame to delete
    When I delete the videogame
    Then the videogame should be deleted successfully

  Scenario: Get a videogame by non-existent ID
    When I get details of the videogame with a non-existent id
    Then I should receive a 404 status code

  Scenario: Create a videogame with missing fields
    When I create a new videogame with missing fields
    Then I should receive a 400 status code
