Feature: Withdraw Fixed Amount
The "Withdraw Cash" menu contains several fixed amounts to
speed up transactions for users.

Scenario: Withdraw fixed amount of $50
   Given I have $500 in my account
   When I choose to withdraw the fixed amount of $50
   Then I should receive $50 cash
       And the balance of my account should be $450


Scenario: Withdraw fixed amount of $150
   Given I have $500 in my account
   When I choose to withdraw the fixed amount of $150
   Then I should receive $150 cash
       And the balance of my account should be $350

  Scenario: Withdraw fixed amount of $250
   Given I have $500 in my account
   When I choose to withdraw the fixed amount of $250
   Then I should receive $250 cash
       And the balance of my account should be $250
