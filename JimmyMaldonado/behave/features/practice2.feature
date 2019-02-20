# Suppose you are going to test
# the form to create a new Gmail
# account :
#
# Add the feature file and the
# scenarios for your testing, in
# your steps verify that
# arguments received for each
# field are specific (e.g.
# Birthday Year only numbers,
# etc, etc)

Feature: Create Gmail account

  Scenario: Verify Gmail account can be created
    Given I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill 'Juan' in First Name field
      And I fill 'Perez' in Last Name field
      And I fill 'juan.perez' in Username field
      And I fill 'Control123' in Password field
      And I fill 'Control123' in Confirm field
      And I select 'Jan' in Month dropdown
      And I fill '25' in Day field
      And I fill '2000' in Year field
      And I select 'Male' in Gender dropdown
      And I fill '123456789' in Mobile Phone field
      And I click on Save button
    Then the message 'Your account was created successfully' is displayed

  Scenario: Verify error message is displayed for duplicated username
    Given I have the user 'pepito.perez' created
      And I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill 'pepito.perez' in Username field
      And I click on Save button
    Then the message 'The account already exists!!' is displayed

  Scenario: Verify messages about required fields are displayed
    Given I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill ' ' in First Name field
      And I click on Save button
    Then the message 'First Name is required!!' is displayed
    When I fill ' ' in Last Name field
      And I click on Save button
    Then the message 'Last Name is required!!' is displayed
    When I fill ' ' in Username field
      And I click on Save button
    Then the message 'Username is required!!' is displayed
    When I fill ' ' in Password field
      And I click on Save button
    Then the message 'Password is required!!' is displayed
    When I fill ' ' in Confirm field
      And I click on Save button
    Then the message 'Confirm is required!!' is displayed

  Scenario: Verify error message when Password and Confirm fields don't match
    Given I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill 'Juan' in First Name field
      And I fill 'Perez' in Last Name field
      And I fill 'juan.perez' in Username field
      And I fill 'Control123' in Password field
      And I fill '123Control' in Confirm field
      And I click on Save button
    Then the message 'Your password does not match!!' is displayed

  Scenario: Verify error message for a year before 1900
    Given I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill 'Juan' in First Name field
      And I fill 'Perez' in Last Name field
      And I fill 'juan.perez' in Username field
      And I fill 'Control123' in Password field
      And I fill 'Control123' in Confirm field
      And I select 'Jan' in Month dropdown
      And I fill '25' in Day field
      And I fill '1899' in Year field
      And I select 'Male' in Gender dropdown
      And I fill '123456789' in Mobile Phone field
      And I click on Save button
    Then the message 'Invalid year!!' is displayed


    Scenario: Verify error message for an invalid Current Email Address
    Given I go to 'https://www.google.com/gmail'
      And I click on CREATE AN ACCOUNT link
    When I fill 'Juan' in First Name field
      And I fill 'Perez' in Last Name field
      And I fill 'juan.perez' in Username field
      And I fill 'Control123' in Password field
      And I fill 'Control123' in Confirm field
      And I select 'Jan' in Month dropdown
      And I fill '25' in Day field
      And I fill '1899' in Year field
      And I select 'Male' in Gender dropdown
      And I fill '123456789' in Mobile Phone field
      And I fill 'invalid.com' in Your current email address field
      And I click on Save button
    Then the message 'Invalid current email address!!. Use the format user@domain.com' is displayed