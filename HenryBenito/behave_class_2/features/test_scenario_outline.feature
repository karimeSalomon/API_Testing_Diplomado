Feature: Withdraw Fixed Amount
  The "Withdraw Cash" menu contains several fixed amounts to
  speed up transactions for users.

  Scenario Outline: Withdraw fixed amount of $50
    Given I have $<Balance> in my account
    When I choose to withdraw the fixed amount of $<Withdrawal/Received>
    Then I should receive $<Withdrawal/Received> cash
    And the balance of my account should be $<Remaining>
    Examples:
      | Balance | Withdrawal/Received | Remaining |
      | 500     | 50                  | 450       |
      | 500     | 150                 | 350       |
      | 500     | 250                 | 250       |
