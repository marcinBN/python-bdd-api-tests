# Template for RestAPI tests with BDD
###### Based on Python, pytest and Gherkin

To do:
- [x] Gherking scenarios
- [x] Deserializing API response to DTO
- [ ] Custom logging


## FEATURES

+ Cucumber-style scenarios
```python
  @details
  Scenario Outline: Get details of a specific videogame-new
    When I get details of the videogame with id <videogame_id>
    Then I should see the videogame name "<expected_name>"

    Examples:
      | videogame_id | expected_name   |
      | 1            | Resident Evil 4 |
      | 2            | Gran Turismo 3  |
```

+ Defining different environments with CLI parameters
```bash
pytest --env prod
```

+ HTML reporting
```bash
pytest --html=report.html
```
