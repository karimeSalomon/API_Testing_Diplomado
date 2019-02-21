Feature: Withdraw Fixed Amount
    Scenario: Withdraw fixed amounts
    Given I have $500 in my account
    When I choose to withdraw the fixed amount of $50
    Then I should receive $50 cash
        And the Balance of my account should be $450
        
    Scenario: Withdraw fixed amounts
    Given I have $500 in my account
    When I choose to withdraw the fixed amount of $100
    Then I should receive $100 cash
        And the Balance of my account should be $400
        
    Scenario: Withdraw fixed amounts
    Given I have $500 in my account
    When I choose to withdraw the fixed amount of $200
    Then I should receive $200 cash
        And the Balance of my account should be $300
