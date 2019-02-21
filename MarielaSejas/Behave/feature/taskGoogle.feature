Feature: Test Google
As an user of the Google I want to search information insert a text and I got information related to search
  Scenario: Successfully display the google search
  Given   I insert the link of Google in teh Browser
    But   My link inserted is incorrect
    When  I enter with the keyboard in the browser
    Then  I see the google page for search

  Scenario: Search to page in Google
  Given  I insert the text that will be to search
    But  my text inserted is incorrect
  When   I select the one of the options displayed
    And  I click on search button
  Then   I have the information that will be search