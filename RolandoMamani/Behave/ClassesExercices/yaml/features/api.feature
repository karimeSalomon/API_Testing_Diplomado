Feature: API

  Scenario:
    Given I have connection to "http://todo.ly"
    When I GET
    Then I receive status code 200