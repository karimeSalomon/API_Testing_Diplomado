Feature: This is the feature title
This is the description of the feature, which can span multiple lines.
You can even include empty lines, like this one:

In fact, everything until the next Gherkin keyword is included in the description.
The text immediately following on the same line as the Feature keyword is the
name of the feature, and the remaining lines are its description.

  Scenario: Successful withdrawal from an account in credit
    Given I insert my PIN
    Given I have $100 on my account
    When I select withdrawal
    When I request $20
    Then $20 should be dispensed
    Then the balance is 80$
