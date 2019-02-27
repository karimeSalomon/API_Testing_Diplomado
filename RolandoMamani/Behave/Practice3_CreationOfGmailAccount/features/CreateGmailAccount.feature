#
#=============================================================================================================================================================================
#Suppose you are going to test the form to create a new gmail account :
#Add the feature file and the scenarios for your testing, in your steps verify that arguments received for each field are specific (e.g. Birthday Year only numbers, etc, etc)
#=============================================================================================================================================================================
#

# Author: Rolando Mamani claros

  Feature: Gmail account creation.
    As a QE I want to enter all required data for a new user account in Gmail in order to have created a new Gmail account

  Scenario Outline: Create new account in Gmail
      Given in Gmail form, the First <Name> of a person
        Examples:
        |Name|
        |Raul|
      And giving also the <Last Name> of the same person
        Examples:
        |Last Name|
        |Terrazas|
      And entering the <user name> for the account
        Examples:
        |user name|
        |r.terrazas|
      And entering a <password>
        Examples:
        |password|
        |Password123|
      And entering the same <previous password>
        Examples:
        |previous password|
        |Password123|
      And selecting the <Month>, <Day> and the <Year> of birthday
        Examples:
        |Month|Day|Year|
        |January|15|1992|
      And selecting the <Gender>
        Examples:
        |Gender|
        |Male|
      And entering the <Number Of Mobil Phone>
        Examples:
        |Number Of Mobil Phone|
        |5248575|
      And entering the current <Email Address>
    Examples:
        |Email Address|
        |rterrazas@gmail.com|
      When Clicking on create button
      Then New Gmail account should be created with provided information

