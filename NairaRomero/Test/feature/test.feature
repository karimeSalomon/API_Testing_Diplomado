Feature: Testing feature title Create  a group
  Testing the documentation part of a feature
  This section is used to document, information of the feature
  define here the user history
  defined what will be test
  Scenario: Title scenario Create a private group
    Given I insert my PIN
      And I have $100 in my account
    When I select withdrawal
      And I request $20
    Then $20 should be dispensed
      And The balance is $80
