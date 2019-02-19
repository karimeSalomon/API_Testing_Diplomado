Feature:
  Scenario: Successful withdrawal from an account in credit
Given I insert my PIN
Given I have {amount} in my account
When I select withdrawal
When I request $20
Then $20 should be dispensed
Then the balance is 80$
