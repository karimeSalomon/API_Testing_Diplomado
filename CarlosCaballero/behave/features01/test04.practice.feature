# suppose you are going to test the form to create a new gmail account:
# add the feature file and the scenarios for your testing, in your steps verify
# that arguments received for each field are specific
# (e.g. Birthday Year only numbers, etc, etc)

Feature: create a gmail account with the form
the create account form contains: 
    - firstname(string)
    - lastname(string)
    - username(string)
    - password(string)
    - confirm(string)
    - month(int[1-12])
    - day(int[1-31])
    - year(int[1900-2001])
    - gender(string{male,female})
    - country(string{list of nation})
    - phone(string)
    - email(string,email)

    Scenario: Valid first name field
        Given write "Carlos" in first name field
         When first name field leave the focus
         Then first name is valid input

    Scenario: Valid first name field
        Given write "" in first name field
         When first name field leave the focus
         Then first name is not a valid input

    Scenario: Valid first name field
        Given write "0000" in first name field
         When first name field leave the focus
         Then first name is not a valid input

    Scenario: Valid last name field
        Given write "Carlos" in last name field
         When last name field leave the focus
         Then last name is valid input

    Scenario: Valid last name field
        Given write "" in last name field
         When last name field leave the focus
         Then last name is not a valid input

    Scenario: Valid last name field
        Given write "0000" in last name field
         When last name field leave the focus
         Then last name is not a valid input

    Scenario: Valid username field
        Given write "Carlos" in username field
         When username field leave the focus
         Then username is valid input

    Scenario: Valid username field
        Given write "" in username field
         When username field leave the focus
         Then username is not a valid input

    Scenario: Valid username field
        Given write "0000" in username field
         When username field leave the focus
         Then username is not a valid input

