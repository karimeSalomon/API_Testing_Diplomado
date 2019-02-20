Feature: Create gmail account

  Scenario: Fill create account form
    Given I go to gmail
      And I click on Create Account button
    When I fill "first name" text field with "xyz" value
      And I fill "last name" text field with "xyz" value
      And I fill "username" text field with "xyz" value
      And I fill "password" text field with "xyz" value
      And I fill "confirm password" text field with "xyz" value
      And I fill "birthday" date field with "02/10/1985" value
      And I select "gender" select field with "Male" value
      And I fill "mobile" number field with "79652125" value
      And I fill "email" email field with "another@account.com" value
