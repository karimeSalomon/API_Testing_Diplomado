Feature: Gmail Account creation

Scenario: Verify is possible to create an Gmail Account

Given I populate Name field with "Nadim"
And I populate LastName field with "Diaz"
And I populate UserName field with "nadim_diaz"
And I populate Passowrd fields with "Control123"
And I fill the date birth day as "01/23/1992"
And I populate Gender field with "Female"
And I populate Phone Number with "76990445"
And I populate Email field with "nadim1232@gmail.com"
When I press all the provided information
Then the account is created
