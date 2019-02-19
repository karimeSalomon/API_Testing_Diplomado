# Created by Ubaldo Villaseca at 2/18/2019
Feature: Some test

  Scenario: Successful withdrawal from an account in credit
    Given I have 100 in my account
    When I request $20
    Then $20 should be dispensed
