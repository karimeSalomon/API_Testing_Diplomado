Feature: Withdraw Fixed Amount
The "Withdraw Cash" menu contains several fixed amounts to
speed up transactions for users.

Scenario Outline: Withdraw fixed amount of $50
   Given I have <Balance> in my account
   When I choose to withdraw the fixed amount of <Withdraw>
   Then I should receive <receive> cash
         And the balance of my account should be <Remaining>


  Examples:
  | Balance| Withdraw |receive |Remaining |
  |$500| $50|$50 |$450|
  |$100| $20|$20 |$80|
  |$1000| $500|$500 |$80|

