Feature: do a google search
  As a google user I want to be able to do a google search
Scenario: Attempt to search Cars in google main page
Given I Open the google main page
When I enter the cards name in the search field and I press enter button
Then i get the cars information


