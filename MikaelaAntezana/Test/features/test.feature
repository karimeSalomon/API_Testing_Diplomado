Feature: Feature Title

This is the description of the feature
Which can span multiple lines

Scenario: Successful withdrawal from an account in credit
Given I have $100 in my account # the context
When I request $20 # the event(s)
Then $20 should be dispensed # the outcome(s)

Scenario: Successful withdrawal from an account in credit
Given I insert my PIN
   And I have $100 in my account
When I select withdrawal
When I request $20
Then $20 should be dispensed
Then the balance is $80