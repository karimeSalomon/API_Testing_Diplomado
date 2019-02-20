Feature: Google home page

  Scenario: Load home page
    Given Open a Web browser
    When Hit Google URL http://google.com
    Then Google home page is loaded

  Scenario: Search in home page
    Given Home is loaded
    When Type a word in search text field
    Then The list of results is shown

  Scenario: No text does not run search
    Given Home is loaded
    When No word is written in search text field
    Then Nothing happens
