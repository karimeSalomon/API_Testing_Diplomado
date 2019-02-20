Feature: Test
 This is the description of the feature, which can span multiple lines.
 You can even include empty lines, like this one:

 Scenario: Successful withdrawal from an account in credit

   Given I have $100 in my account # the context precondicion
   When  I request $20 # the event(s) #cuando le pido 20 dolares
   Then  $20 should be dispensed # the outcome(s) #deberia de tener 20 dolares

  Scenario: Successful withdrawal from an account in credit
   Given I insert my PIN
   And   I have $100 in my account
   When  I select withdrawal
   And   I request $20
   Then  $20 should be dispensed
   And   the balance is 80$