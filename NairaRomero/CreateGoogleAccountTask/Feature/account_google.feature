Feature: Create a Google gmail account
  Scenario:
    As a user I want to create a google gmail account with valid inputs and and required inputs so I get a google gmail account
    Given I in https://accounts.google.com page

    When I click on Create Account button
    And I write my first name with "Naira"
    And I write my las name with "Romero"
    And I write a valid username with "naira88re"
    And I write a valid password with "Control123"
    And I write to confirm the password again with  "Control123"
    And I chose a month of birthday from the dropdown "12"
    And I write a day of birthday "26"
    And I write a year of birthday "1990"
    And I select a Gender from  the Gender dropdown like "Female"
    And I write a valid Mobile Phone like "743363489"
    And I write a current email address like "Bejing av. and America #123 "
    And I press Enter
    Then I created my new google gmail account

    """Scenario: attempt to Create a gmail account without required fields like birthday and gender
      As a user I attemp to create a google gmail account without fill all the required fields like birthday and gender so that I cannot create new account
        Given I in https://accounts.google.com page
        When I click on Create Account button
        And I write my first name with "Mario"
        And I write my las name with "Perez"
        And I write a valid username with "mario88re"
        And I write a valid password with "Control345"
        And I write to confirm the password again with  "Control345"
        And I chose a month of birthday from the dropdown ""
        And I write a day of birthday ""
        And I write a year of birthday ""
        And I select a Gender from  the Gender dropdown like ""
        And I write a valid Mobile Phone like "743456789"
        And I write a current email address like "Bejing av. and Simon Lopez #456 "
        And I press Enter
        Then I am unable to created my a new google gmail account without filling the gender and birthday inputs

     Scenario: Attemp to create gmail account with an existing user name
      As a user I attemp to create a google gmail account with a user name that already exists so that I am not enable to create an account
      Given I in https://accounts.google.com page
      When I click on Create Account button
        And I write my first name with "Mario"
        And I write my las name with "Perez"
        But I write a invalid username "naria88re" that already exists
        And I write a valid password with "Control345"
        And I write to confirm the password again with  "Control345"
        And I chose a month of birthday from the dropdown "11"
        And I write a day of birthday "25"
        And I write a year of birthday "1991"
        And I select a Gender from  the Gender dropdown like "Male"
        And I write a valid Mobile Phone like "743456789"
        And I write a current email address like "Bejing av. and Simon Lopez #456 "
        And I press Enter
      Then I am not enable to create a google gmail account with an already existing username

     Scenario:
      As a user I attemp to create a google gmail account with a invalid password that has less than 8 characters so I am not enable to create an account
      Given I in https://accounts.google.com page
      When I click on Create Account button
        And I write my first name with "Maria"
        And I write my las name with "Perez"
        And I write a valid username with "maria123"
        But I write a invalid password "cotro1" that has less than 7 characters
        And I write to confirm the password again with  "cotro1"
        And I choose a month of birthday from the dropdown "10"
        And I write a day of birthday "24"
        And I write a year of birthday "1992"
        And I select a Gender from  the Gender dropdown like "Male"
        And I write a valid Mobile Phone like "743456789"
        And I write a current email address like "Melchor av. and Simon Lopez #678 "
        And I press Enter
      Then I am not enable to create the account with an invalid password """
