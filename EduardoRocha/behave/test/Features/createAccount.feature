feature Create a new account
  As a google user I want to be able to create a new account
Scenario: Attempt to create a new account
Given I Open the Gmail main page to create a new accounts
Given I have a valid Name and Last Name
Given I choose a new valid username
Given I have a valid password
Given I have a Valid Mobile phone
Given I have a current email address
When enter the name to Name field
and enter the lastName to Last field
and enter the valid username
and enter the password to create a password and confirm your password fields
and select a valid month, day , year on Birthday fields
and select th e Gender
and enter the mobile phone number to mobile phone field
and enter a current email address to your current email address field

and click on create button
Then the successfully created account message should be shown
