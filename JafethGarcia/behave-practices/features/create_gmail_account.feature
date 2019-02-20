Feature: Create new Gmail Account

  Scenario: Account is created for a new username
    Given I insert Jhon as first name
    And I insert Doe as last name
    And I insert jhon.doe as username
    And I insert sshsecret as password
    And I insert sshsecret as confirm password
    And I insert may 18 of 1985 as birthday date
    And I insert 5916782738 as a mobile phone
    And I insert jhon.doe.creator@gmail.com as email address
    When I click on submit button
    Then An account with username as jhon.doe is created
  
  Scenario: Account cannot be created with existing username
    Given I insert Jhon as first name
    And I insert Doe as last name
    And I insert jhon.doe.creator as username
    And I insert othersecret as password
    And I insert othersecret as confirm password
    And I insert may 18 of 1985 as birthday date
    And I insert 591695842 as a mobile phone
    And I insert jhon.doe.creator@gmail.com as email address
    When I click on submit button
    Then An account with username as jhon.doe.creator is not created
  
  Scenario: Validation error is shown with invalid email
    Given I insert Jhon as first name
    And I insert Doe as last name
    And I insert jhon.doe as username
    And I insert sshsecret as password
    And I insert sshsecret as confirm password
    And I insert may 18 of 1985 as birthday date
    And I insert 5916782738 as a mobile phone
    And I insert jhon.doe.creatorgmail.com as email address
    When I click on submit button
    Then An account with username as jhon.doe is not created

  Scenario: Validation error is shown with invalid confirm password
    Given I insert Jhon as first name
    And I insert Doe as last name
    And I insert jhon.doe as username
    And I insert sshsecret as password
    And I insert sshsoppsecret as confirm password
    And I insert may 18 of 1985 as birthday date
    And I insert 5916782738 as a mobile phone
    And I insert jhon.doe.creator@gmail.com as email address
    When I click on submit button
    Then An account with username as jhon.doe is not created
  