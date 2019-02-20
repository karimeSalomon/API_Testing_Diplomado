Feature: Withdraw Fixed amount
  The Withdraw cash menu contains several fixed amounts to
  spedd up transaction for users.
  Scenario: Withdraw fixed amount of $50
    Given i have $500 in my account
    When i choose to withdraw the fixed amount of $50
    Then i should receive $50 cash
    And the balance of my account should be $450

   Scenario: Withdraw fixed amount of $100
    Given i have $500 in my account
    When i choose to withdraw the fixed amount of $100
    Then i should receive $100 cash
    And the balance of my account should be $400

    Scenario: Withdraw fixed amount of $200
    Given i have $500 in my account
    When i choose to withdraw the fixed amount of $200
    Then i should receive $200 cash
    And the balance of my account should be $300