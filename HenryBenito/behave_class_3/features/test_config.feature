Feature: config
  Scenario: Play with config
    Given I have connection to "http://todo.ly"
    When I GET
    Then I receive status code 200