Feature: Customer search
  Scenario: Search a price value using client name
    Given I get the id of client searching by "Carlos" name
    When I search the id on price list
    Then the price is 6.2
