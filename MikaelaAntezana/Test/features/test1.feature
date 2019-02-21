Feature: Test UI Components in main page

Scenario: Change page language
Given I am located in Google Search page
When clicking over the "Google offered in" language link
Then the language of all labels in the page changes to what was selected

Scenario: Sign Up button opens "Sign In" form
Given I am located in Google Search page
When pressing the "Sign Up" button
Then the "Sign In" page with "Select and account" options displayed on it

Scenario:
Given I am located in Google Search page
When
Then