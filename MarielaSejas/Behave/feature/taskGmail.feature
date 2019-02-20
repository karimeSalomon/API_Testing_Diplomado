Feature: Create gmail account
As an user I want to create an account on gmail
  Scenario: Create account on gmail
  Given  I fill the fields as $Carla
    And  Insert the $Cespedes
    And  Insert the $carl
    And  Insert the $123
    And  Insert the $123
    And  Insert the $28Enero
    And  Insert the $Femenino
    And  Insert the $123445
  When   I select the one of the options displayed
    And  I click on submit button
  Then   I have the account created