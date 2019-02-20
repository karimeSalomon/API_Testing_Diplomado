# Suppose you are going to test
# the form to create a new gmail
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


