@banking
Feature: Authentication

  @deposit
  Scenario: Authenticate with valid credentials
    When I authenticate with valid credentials
    Then I should receive a valid authentication token